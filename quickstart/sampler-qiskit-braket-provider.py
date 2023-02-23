from qiskit_braket_provider import AWSBraketProvider
from qiskit.primitives import BackendSampler

provider = AWSBraketProvider()
backend = provider.backends("SV1")
sampler = BackendSampler(backend)