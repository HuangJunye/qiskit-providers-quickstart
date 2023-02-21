from qiskit_braket_provider import AWSBraketProvider
from qiskit.primitives import BackendEstimator

provider = AWSBraketProvider()
backend = provider.backends("SV1")
estimator = BackendEstimator(backend)