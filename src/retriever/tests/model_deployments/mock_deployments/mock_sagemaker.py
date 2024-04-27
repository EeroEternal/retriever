import json
from typing import Any, Dict, Generator, List

from cohere.types import StreamedChatResponse

from retriever.chat.custom.model_deployments.base import BaseDeployment
from retriever.chat.enums import StreamEvent
from retriever.schemas.cohere_chat import CohereChatRequest


class MockSageMakerDeployment(BaseDeployment):
    """SageMaker Deployment"""

    DEFAULT_MODELS = ["command-r"]

    @property
    def rerank_enabled(self) -> bool:
        return False

    @classmethod
    def list_models(cls) -> List[str]:
        return cls.DEFAULT_MODELS

    @classmethod
    def is_available(cls) -> bool:
        return True

    def invoke_chat_stream(
        self, chat_request: CohereChatRequest, **kwargs: Any
    ) -> Generator[StreamedChatResponse, None, None]:
        events = [
            {
                "event_type": StreamEvent.STREAM_START,
                "generation_id": "test",
                "is_finished": False,
            },
            {
                "event_type": StreamEvent.TEXT_GENERATION,
                "text": "This is a test.",
                "is_finished": True,
            },
            {
                "event_type": StreamEvent.STREAM_END,
                "is_finished": True,
                "generation_id": "test",
                "citations": [],
                "documents": [],
                "search_results": [],
                "search_queries": [],
                "finish_reason": "MAX_TOKENS",
            },
        ]

        for event in events:
            yield event

    def invoke_search_queries(
        self,
        message: str,
        chat_history: List[Dict[str, str]] | None = None,
        **kwargs: Any
    ) -> list[str]:
        pass

    def invoke_rerank(
        self, query: str, documents: List[Dict[str, Any]], **kwargs: Any
    ) -> Any:
        return None