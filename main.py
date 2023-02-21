providers = ['qiskit-terra', 'qiskit-ibm-runtime', 'qiskit-braket-provider']
algorithms = ['bell', 'vqe']


def generate_examples(provider, algorithm):

    code= {
        'provider': {},
        'algorithm': {}
    }

    code['provider']['qiskit-terra'] = """# Instantiate sampler
from qiskit.primitives import Sampler
sampler = Sampler()
"""
    code['provider']['qiskit-ibm-runtime'] = """# Instantiate sampler
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
sampler = Sampler(session=backend)
"""
    code['provider']['qiskit-braket-provider'] = """# Instantiate sampler
from qiskit_braket_provider import AWSBraketProvider
from qiskit.primitives import BackendSampler

provider = AWSBraketProvider()
backend = provider.backends("SV1")
sampler = BackendSampler(backend)
"""

    code['algorithm']['bell'] = """# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Run the circuit and get result distribution
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
print(quasi_dist)
"""

    code ['algorithm']['vqe'] = """# Create H2 molecule 
from qiskit.quantum_info import SparsePauliOp

H2_op = SparsePauliOp.from_list([
    ("II", -1.052373245772859),
    ("IZ", 0.39793742484318045),
    ("ZI", -0.39793742484318045),
    ("ZZ", -0.01128010425623538),
    ("XX", 0.18093119978423156)
])

# Calculate ground state energy using VQE
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import SLSQP
from qiskit.algorithms.minimum_eigensolvers import VQE

ansatz = TwoLocal(2, "ry", "cz")
optimizer = SLSQP(maxiter=1000)
vqe = VQE(estimator, ansatz, optimizer)
result = vqe.compute_minimum_eigenvalue(operator=H2_op)
print(result.eigenvalue)
"""
    
    code_example = code['provider'][provider] + '\n' + code['algorithm'][algorithm]
    print(code_example)

if __name__ == '__main__':
    for provider in providers:
        for algorithm in algorithms:
            print("###################################################")
            print(f'Provider: {provider} running algorithm {algorithm}')
            print("###################################################")
            generate_examples(provider, algorithm)
