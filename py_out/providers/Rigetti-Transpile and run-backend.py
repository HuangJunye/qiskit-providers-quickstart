from qiskit_rigetti import RigettiQCSProvider
provider = RigettiQCSProvider()
backend = provider.get_backend(name="Aspen-9")

# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Transpile circuit
from qiskit import transpile
transpiled_circuit = transpile(circuit, backend)

# Run the circuit and get result
job = backend.run(transpiled_circuit)
counts = job.result().get_counts()
print(counts)