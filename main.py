providers = ['qiskit-terra', 'qiskit-ibm-runtime', 'qiskit-braket-provider']
algorithms = ['bell', 'vqe']


def generate_examples(provider, algorithm):

    code= {
        'provider': {},
        'algorithm': {}
    }

    code_example = code['provider'][provider] + '\n' + code['algorithm'][algorithm]
    print(code_example)

if __name__ == '__main__':
    for provider in providers:
        for algorithm in algorithms:
            print("###################################################")
            print(f'Provider: {provider} running algorithm {algorithm}')
            print("###################################################")
            generate_examples(provider, algorithm)
