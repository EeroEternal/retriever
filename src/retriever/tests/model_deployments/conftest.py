from unittest.mock import patch

import pytest
from sqlalchemy.orm import Session

from retriever.models.user import User
from retriever.tests.factories import get_factory
from retriever.tests.model_deployments.mock_deployments import (
    MockAzureDeployment,
    MockCohereDeployment,
    MockSageMakerDeployment,
)


@pytest.fixture()
def user(session_chat: Session) -> User:
    return get_factory("User", session_chat).create()


@pytest.fixture()
def mock_cohere_deployment():
    with patch("retriever.chat.custom.custom.get_deployment") as mock:
        mock.return_value = MockCohereDeployment()
        yield mock


@pytest.fixture()
def mock_sagemaker_deployment():
    with patch("retriever.chat.custom.custom.get_deployment") as mock:
        mock.return_value = MockSageMakerDeployment()
        yield mock


@pytest.fixture()
def mock_azure_deployment():
    with patch("retriever.chat.custom.custom.get_deployment") as mock:
        mock.return_value = MockAzureDeployment()
        yield mock
