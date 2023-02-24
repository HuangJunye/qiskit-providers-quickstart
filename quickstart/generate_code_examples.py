import os
import yaml
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_dict = yaml.safe_load(yaml_in)

with open(os.path.join(yaml_dir, 'providers'+'.yaml'), 'r') as yaml_in:
    providers_dict = yaml.safe_load(yaml_in)

code = []
code.append(providers_dict[0]['code'])
code.append('\n')
code.append(algorithms_dict[0]['code'])
code = ''.join(code)
print(code)
