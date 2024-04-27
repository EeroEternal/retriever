from retriever.chat.custom.model_deployments.azure import AzureDeployment
from retriever.chat.custom.model_deployments.cohere_platform import CohereDeployment
from retriever.chat.custom.model_deployments.deployment import get_deployment
from retriever.chat.custom.model_deployments.sagemaker import SageMakerDeployment

__all__ = [
    "AzureDeployment",
    "CohereDeployment",
    "SageMakerDeployment",
    "get_deployment",
]
