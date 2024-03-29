import os
import yaml
import json
from pprint import pprint

script_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(script_dir, "yaml_in")
providers_dir = os.path.join(yaml_dir, "providers")
json_dir = os.path.join(script_dir, "json_out")
providers_json_dir = os.path.join(json_dir, "providers")
py_dir = os.path.join(script_dir, "py_out")
quick_start_py_dir = os.path.join(py_dir, "quick-start")

with open(os.path.join(yaml_dir, 'algorithms'+'.yaml'), 'r') as yaml_in:
    algorithms_list = yaml.safe_load(yaml_in)

quick_start_list = []

for category in sorted(os.listdir(providers_dir)):
    with open(os.path.join(providers_dir, category), 'r')as yaml_in:
        category_dict = yaml.safe_load(yaml_in)
        providers_list = category_dict['providers']

        for provider in providers_list:

            # add 'pip install qiskit' to all installation command
            if provider['title'] == 'Qiskit Stand-alone':
                provider['installation'] = ['pip install qiskit']
            else: 
                provider['installation'] = [
                    'pip install qiskit',
                    provider['installation']
                ]
            
            provider_setup_code = []
            provider['codeExamples'] = []

            for algorithm in algorithms_list:
                algorithm_code = algorithm['code'].splitlines()

                if algorithm['runMethod'] == 'backend':
                    if algorithm['name'] == 'Transpiling':
                        if provider['title'] == 'Qiskit Stand-alone':
                            # specify basis gates for qiskit stand-alone
                            algorithm_code = [
                                "# Build circuit",
                                "from qiskit.circuit.library import QuantumVolume",
                                "circuit = QuantumVolume(5)",
                                "",
                                "# Transpile circuit",
                                "from qiskit import transpile",
                                "transpiled_circuit = transpile(circuit, basis_gates=['sx', 'rz', 'cx'])",
                                "transpiled_circuit.draw()"
                            ]
                            # do not use basic aer
                            provider_setup_code = []
                        elif provider['code'].get('backend'):
                            provider_setup_code = provider['code']['backend'].splitlines()
                        else:
                            algorithm_code = []
                    else:
                        algorithm_code = []
                else:
                    # primitive.run
                    if provider['code'].get('sampler'):
                        # native primitive support
                        provider_setup_code = provider['code']['sampler'].splitlines()
                    else:
                        # no native primitive support, wrap backend into backend primitive
                        provider_setup_code = provider['code']['backend'].splitlines()
                        provider_setup_code.insert(1, 'from qiskit.primitives import BackendSampler')
                        provider_setup_code.append('sampler = BackendSampler(backend)')

                if provider_setup_code:
                    full_code = provider_setup_code + [''] + algorithm_code
                else:
                    full_code = algorithm_code

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
                    # with open(os.path.join(quick_start_py_dir, f'{provider_name}-{algorithm_name}-{algorithm_run_method}.py'), "w") as f:
                    #     f.write(full_code)

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

            if provider['title'] == 'Qiskit Stand-alone':
                qiskit_stand_alone_entry = provider.copy()
            else:
                quick_start_list.append(provider)

# post processing
# 1) sort alphabetically
# 2) remove duplicate entries from different categories
# 3) insert qiskit stand-alone as the first entry

quick_start_list.sort(key=lambda d:d['title'].lower())
# reverse to remove later entries and then reverse back to keep earlier entries
# the first entry in the order of the categories are kept, namely
# primitives > hardware > local simulators > cloud simulators > multi-platforms
quick_start_list = list({i['title']:i for i in reversed(quick_start_list)}.values())
quick_start_list.reverse()
quick_start_list.insert(0, qiskit_stand_alone_entry)


for provider in quick_start_list:
    print("=========================")
    print(provider['title'])
    #pprint(provider['codeExamples'][0])

with open(os.path.join(json_dir, "quick-start.json"), "w") as json_out:
    print(f"We have {len(quick_start_list)} providers.")
    json.dump(quick_start_list, json_out, indent=2)
