import os
import yaml
import json

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
providers_dir = os.path.join(yaml_dir, "providers")
json_dir = os.path.join(script_dir, "json_out")
providers_json_dir = os.path.join(json_dir, "providers")
py_dir = os.path.join(script_dir, "py_out")
providers_py_dir = os.path.join(py_dir, "providers")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_list = yaml.safe_load(yaml_in)

for category in os.listdir(providers_dir):
    with open(os.path.join(providers_dir, category), 'r')as yaml_in,\
         open(os.path.join(providers_json_dir, category[:-4]+"json"), "w") as json_out:
        category_dict = yaml.safe_load(yaml_in)
        providers_list = category_dict['providers']

        for provider in providers_list:
            provider_setup_code = []
            provider['codeExamples'] = []

            # only use the first entry of the algorithms for providers page
            if provider['code'].get('backend'):
                algorithm = algorithms_list[0]
                provider_setup_code = provider['code']['backend'].splitlines()
            else:
                algorithm = algorithms_list[1]
                provider_setup_code = provider['code']['sampler'].splitlines()
                
            algorithm_code = algorithm['code'].splitlines()

            full_code = provider_setup_code + [''] + algorithm_code

            # input code example for each provider uses sampler by default
            # if the algorithm runs with estimator, we replace 'sampler' with 'estimator'
            # join list of strings into a long string so that we can do text replacement with one call
            full_code = '\n'.join(full_code)
            if algorithm['runMethod'] == 'estimator':
                full_code = full_code.replace('sampler', 'estimator')
                full_code = full_code.replace('Sampler', 'Estimator')

            provider_name = provider['title']
            algorithm_name = algorithm['name']
            algorithm_run_method = algorithm['runMethod']

            if full_code:
                with open(os.path.join(providers_py_dir, f'{provider_name}-{algorithm_name}-{algorithm_run_method}.py'), "w") as f:
                    f.write(full_code)

                temp = full_code.splitlines()
                # make a copy here because we want to drop the unwanted 'code' entry without
                # affecting the subsequent loops
                algorithm_entry = algorithm.copy()
                # use "&nbsp;" for empty line as requested by front-end
                algorithm_entry['fullCode'] = ["&nbsp;" if line == "" else line for line in temp]
                # drop unwanted 'code' entry
                del algorithm_entry['code']
                provider['codeExamples'].append(algorithm_entry)
            # drop unwanted 'code' entry
            del provider['code']

        json.dump(category_dict, json_out, indent=2)
