from qiskit_ionq import IonQProvider
provider = IonQProvider("MY_IONQ_TOKEN")
backend = provider.get_backend("ionq_simulator")

# Build and transpile circuit
from qiskit import QuantumCircuit, transpile
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])
transpiled_circuit = transpile(circuit, backend)

# Run the circuit and get result
job = backend.run(transpiled_circuit)
counts = job.result().get_counts()
print(counts)