import os
import yaml
import json

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml")
json_dir = os.path.join(script_dir, "json")

for filename in os.listdir(yaml_dir):
    with open(os.path.join(yaml_dir, filename), 'r') as yaml_in, open(os.path.join(json_dir, filename[:-4]+"json"), "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
        for provider in yaml_object:
            # split multiline string into a list of strings
            temp = provider['helloWorldExample'].splitlines()
            # replace empty line with "&nbsp;"
            provider['helloWorldExample'] = ["&nbsp;" if item == "" else item for item in temp]

        json.dump(yaml_object, json_out, indent=2)
