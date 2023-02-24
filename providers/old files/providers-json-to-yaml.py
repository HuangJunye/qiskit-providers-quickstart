import os
import yaml
import json

script_dir = os.path.dirname(__file__)
json_dir = os.path.join(script_dir, "json_in")
yaml_dir = os.path.join(script_dir, "yaml_out")

# dump multiline string using '|' style
def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

for filename in os.listdir(json_dir):
    with open(os.path.join(json_dir, filename), 'r') as json_in, open(os.path.join(yaml_dir, filename[:-4]+"yaml"), "w") as yaml_out:
        json_object = json.load(json_in)
        for provider in json_object:
            temp = provider['helloWorldExample']
            provider['helloWorldExample'] = ''.join(temp)
            print(provider['helloWorldExample'])
        yaml.safe_dump(json_object, yaml_out, sort_keys=False)
