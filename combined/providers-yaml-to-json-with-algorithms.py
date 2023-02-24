import os
import yaml
import json
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
json_dir = os.path.join(script_dir, "json_out")
py_dir = os.path.join(script_dir, "py_out")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_list = yaml.safe_load(yaml_in)

with open(os.path.join(yaml_dir, 'providers'+'.yaml'), 'r') as yaml_in:
    providers_list = yaml.safe_load(yaml_in)

code_examples_list = []

for provider in providers_list:
    
    provider_code = []

    for algorithm in algorithms_list:

        algorithm_code = []

        if algorithm['runMethod'] == 'backend':
            if provider['code']['support_backend_run']:
                provider_code = provider['code']['backend'].splitlines()
        else:
            if provider['code']['support_primitives']:
                provider_code = provider['code']['sampler'].splitlines()
            else:
                provider_code = provider['code']['backend'].splitlines()
                provider_code.insert(1, 'from qiskit.primitives import BackendSampler')
                provider_code.append('sampler = BackendSampler(backend)')

        algorithm_code = algorithm['code'].splitlines()
        
        code = provider_code + [''] + algorithm_code
        code = '\n'.join(code)

        if algorithm['runMethod'] == 'estimator':
            code = code.replace('sampler', 'estimator')
            code = code.replace('Sampler', 'Estimator')

        provider_name = provider['title']
        algorithm_name = algorithm['name']
        algorithm_run_method = algorithm['runMethod']

        with open(os.path.join(py_dir, f'{provider_name}-{algorithm_name}-{algorithm_run_method}.py'), "w") as f:
            f.write(code)

        temp = code.splitlines()
        algorithm['full_code'] = ["&nbsp;" if line == "" else line for line in temp]

        code_examples_list.append(algorithm)

pprint(code_examples_list)

json_out = open(os.path.join(json_dir, "test.json"), "w")
json.dump(code_examples_list, json_out, indent=2)
