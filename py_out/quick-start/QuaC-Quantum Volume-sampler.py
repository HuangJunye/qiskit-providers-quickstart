from quac_qiskit import Quac
from qiskit.primitives import BackendSampler
backend = Quac.get_backend("fake_vigo_density_simulator")
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