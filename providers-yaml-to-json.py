import yaml
import json

with open("providers.yaml", 'r') as yaml_in, open("providers.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
    for provider in yaml_object:
        # split multiline string into a list of strings
        temp = provider['helloWorldExample'].splitlines()
        # replace empty line with "&nbsp;"
        provider['helloWorldExample'] = ["&nbsp;" if item == "" else item for item in temp]

    json.dump(yaml_object, json_out, indent=2)
