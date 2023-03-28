import strangeworks
from qiskit.primitives import BackendSampler
from strangeworks_qiskit import StrangeworksProvider
# get your API key from the Strangeworks Portal
strangeworks.authenticate(api_key="your-api-key")
provider = StrangeworksProvider()
backend = provider.get_backend("ibmq_qasm_simulator")
sampler = BackendSampler(backend)

# Build circuit
from qiskit.circuit.library import QuantumVolume
circuit = QuantumVolume(5)
circuit.measure_all()

# Run the circuit and plot result distribution
from qiskit.visualization import plot_histogram
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
plot_histogram(quasi_dist)