from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from retriever.models.base import Base
from retriever.models.file import File
from retriever.models.message import Message


class Conversation(Base):
    __tablename__ = "conversations"

    user_id: Mapped[str]
    title: Mapped[str] = mapped_column(String, default="New Conversation")
    description: Mapped[str] = mapped_column(String, nullable=True, default=None)

    text_messages: Mapped[List["Message"]] = relationship()
    files: Mapped[List["File"]] = relationship()

    @property
    def messages(self):
        return sorted(self.text_messages, key=lambda x: x.position)
