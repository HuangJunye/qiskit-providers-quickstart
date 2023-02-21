from qiskit_ibm_runtime import QiskitRuntimeService, Estimator
service = QiskitRuntimeService()
backend = service.backend("ibmq_qasm_simulator")
estimator = Estimator(session=backend)