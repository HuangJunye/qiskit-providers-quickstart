from qiskit_rigetti import RigettiQCSProvider
from qiskit.primitives import BackendSampler
provider = RigettiQCSProvider()
backend = provider.get_backend(name="Aspen-9")
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