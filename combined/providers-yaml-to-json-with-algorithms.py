import os
import yaml
import json
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
providers_dir = os.path.join(yaml_dir, "providers")
json_dir = os.path.join(script_dir, "json_out")
py_dir = os.path.join(script_dir, "py_out")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_list = yaml.safe_load(yaml_in)

for filename in os.listdir(providers_dir):
    with open(os.path.join(providers_dir, filename), 'r')as yaml_in, open(os.path.join(json_dir, filename[:-4]+"json"), "w") as json_out:
        providers_list = yaml.safe_load(yaml_in)

        code_examples_list = []

        for provider in providers_list:
            
            provider_code = []
            provider['codeExamples'] = []

            for algorithm in algorithms_list:

                algorithm_code = []
                algorithm_code = algorithm['code'].splitlines()

                if algorithm['runMethod'] == 'backend':
                    # backend.run
                    if provider['code'].get('backend'):
                        provider_code = provider['code']['backend'].splitlines()
                    else:
                        # create empty code lines if provider does not support backend run
                        algorithm_code = []
                else:
                    # primitive.run
                    if provider['code'].get('sampler'):
                        # native primitive support
                        provider_code = provider['code']['sampler'].splitlines()
                    else:
                        # no native primitive support, wrap backend into backend primitive
                        provider_code = provider['code']['backend'].splitlines()
                        provider_code.insert(1, 'from qiskit.primitives import BackendSampler')
                        provider_code.append('sampler = BackendSampler(backend)')

                full_code = provider_code + [''] + algorithm_code
                full_code = '\n'.join(full_code)

                if algorithm['runMethod'] == 'estimator':
                    full_code = full_code.replace('sampler', 'estimator')
                    full_code = full_code.replace('Sampler', 'Estimator')

                provider_name = provider['title']
                algorithm_name = algorithm['name']
                algorithm_run_method = algorithm['runMethod']

                if full_code:
                    with open(os.path.join(py_dir, f'{provider_name}-{algorithm_name}-{algorithm_run_method}.py'), "w") as f:
                        f.write(full_code)

                    temp = full_code.splitlines()
                    algorithm['full_code'] = ["&nbsp;" if line == "" else line for line in temp]
                    algorithm_entry = algorithm.copy()
                    del algorithm_entry['code']
                    provider['codeExamples'].append(algorithm_entry)
                    code_examples_list.append(algorithm)

        json.dump(providers_list, json_out, indent=2)
