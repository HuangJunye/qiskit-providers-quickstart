from gaqqie_door import QiskitGaqqie
from qiskit.primitives import BackendSampler
# rewrite to the endpoint URL of the user API
url = "https://<api-id>.execute-api.<region>.amazonaws.com/<stage>"
QiskitGaqqie.enable_account(url)
backend = QiskitGaqqie.get_backend("qiskit_simulator")
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