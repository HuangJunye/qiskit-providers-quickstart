from qiskit_ionq import IonQProvider
from qiskit.primitives import BackendSampler
provider = IonQProvider("MY_IONQ_TOKEN")
backend = provider.get_backend("ionq_simulator")
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