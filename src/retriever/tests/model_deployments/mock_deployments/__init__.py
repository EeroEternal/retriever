from retriever.tests.model_deployments.mock_deployments.mock_azure import (
    MockAzureDeployment,
)
from retriever.tests.model_deployments.mock_deployments.mock_cohere_platform import (
    MockCohereDeployment,
)
from retriever.tests.model_deployments.mock_deployments.mock_sagemaker import (
    MockSageMakerDeployment,
)

__all__ = [
    "MockCohereDeployment",
    "MockSageMakerDeployment",
    "MockAzureDeployment",
]
