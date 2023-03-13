from qiskit_ibm_provider import IBMProvider
from qiskit.primitives import BackendSampler

provider = IBMProvider()
backend = provider.get_backend("ibmq_qasm_simulator")
sampler = BackendSampler(backend)

# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Run the circuit and get result distribution
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
print(quasi_dist)