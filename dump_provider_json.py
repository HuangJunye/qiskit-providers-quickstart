import json

def dump_json_files():

    code= {
    }

    sampler_code = []

    sampler_code['qiskit-ibm-runtime'] = """from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
sampler = Sampler(session=backend)
"""
    sampler_code['qiskit-terra'] = """from qiskit.primitives import Sampler
sampler = Sampler()
"""

    sampler_code['qiskit-braket-provider'] = """from qiskit_braket_provider import AWSBraketProvider
from qiskit.primitives import BackendSampler

provider = AWSBraketProvider()
backend = provider.backends("SV1")
sampler = BackendSampler(backend)
"""

    code['qiskit-ibm-runtime'] = {}

    code['qiskit-ibm-runtime']['sampler'] = string.splitlines()

    string = string.replace('sampler', 'estimator')
    string = string.replace('Sampler', 'Estimator')

    code['qiskit-ibm-runtime']['estimator'] = string.splitlines()

    with open("providers.json", "w") as f:
        json.dump(code, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    dump_json_files()