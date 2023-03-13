from qiskit_quantinuum import Quantinuum
Quantinuum.save_account("username@company.com")
backend = Quantinuum.get_backend("DEVICE_NAME")

# Build and transpile circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])
transpiled_circuit = transpile(circuit, backend)

# Run the circuit and get result
job = backend.run(transpiled_circuit)
counts = job.result().get_counts()
print(counts)