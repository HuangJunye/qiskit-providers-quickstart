from qiskit_aqt_provider import AQTProvider
from qiskit.primitives import BackendSampler
aqt = AQTProvider('MY_TOKEN')
backend = aqt.get_backend('aqt_qasm_simulator')
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