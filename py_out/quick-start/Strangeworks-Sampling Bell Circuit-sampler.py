import strangeworks
from qiskit.primitives import BackendSampler
from strangeworks_qiskit import StrangeworksProvider
# get your API key from the Strangeworks Portal
strangeworks.authenticate(api_key="your-api-key")
provider = StrangeworksProvider()
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