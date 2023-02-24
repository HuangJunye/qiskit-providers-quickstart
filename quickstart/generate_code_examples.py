import os
import yaml
import json
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
json_dir = os.path.join(script_dir, "json_out")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_dict = yaml.safe_load(yaml_in)

with open(os.path.join(yaml_dir, 'providers'+'.yaml'), 'r') as yaml_in:
    providers_dict = yaml.safe_load(yaml_in)

code_dict = {}

for provider, provider_info in providers_dict.items():

    code_dict[provider] = {}

    for algorithm, algorithm_info in algorithms_dict.items():
        code = []
        code.append(providers_dict[provider]['code'])
        code.append('\n')
        code.append(algorithms_dict[algorithm]['code'])
        code = ''.join(code)
        # if the algorithm use estimator instead of the default sampler
        if algorithms_dict[algorithm]['primitive'] == 'estimator':
            code = code.replace('sampler', 'estimator')
            code = code.replace('Sampler', 'Estimator')

        temp= code.splitlines()
        code_dict[provider][algorithm] = ["&nbsp;" if line == "" else line for line in temp]


json_out = open(os.path.join(json_dir, "quickstart.json"), "w")
json.dump(code_dict, json_out, indent=2)
    
        