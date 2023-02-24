import os
import yaml
import json
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
json_dir = os.path.join(script_dir, "json_out")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_list = yaml.safe_load(yaml_in)

with open(os.path.join(yaml_dir, 'providers'+'.yaml'), 'r') as yaml_in:
    providers_list = yaml.safe_load(yaml_in)

code_examples_list = []

for provider in providers_list:
    
    for algorithm in algorithms_list:

        provider_code = []
        algorithm_code = []

        if algorithm['runMethod'] == 'backend' and provider['code']['support_backend_run']:
            provider_code = provider['code']['backend'].splitlines()
            algorithm_code = algorithm['code'].splitlines()

        code = provider_code + [''] + algorithm_code
        code = '\n'.join(code)


        temp = code.splitlines()
        algorithm['full_code'] = ["&nbsp;" if line == "" else line for line in temp]

        code_examples_list.append(algorithm)

pprint(code_examples_list)