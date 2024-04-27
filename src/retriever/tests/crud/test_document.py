import pytest

from retriever.crud import document as document_crud
from retriever.models.document import Document
from retriever.tests.factories import get_factory

# from retriever.schemas.document import UpdateDocument


@pytest.fixture(autouse=True)
def conversation(session):
    return get_factory("Conversation", session).create(id="1")


@pytest.fixture(autouse=True)
def message(session, conversation):
    return get_factory("Message", session).create(
        id="1", text="Hello, World!", conversation_id="1"
    )


def test_create_document(session):
    document_data = Document(
        text="Hello, World!",
        user_id="1",
        conversation_id="1",
        url="https://www.example.com",
        document_id="1",
        message_id="1",
    )

    document = document_crud.create_document(session, document_data)
    assert document.text == document_data.text
    assert document.user_id == document_data.user_id
    assert document.conversation_id == document_data.conversation_id
    assert document.url == document_data.url
    assert document.document_id == document_data.document_id
    assert document.message_id == document_data.message_id

    document = document_crud.get_document(session, document.id)
    assert document.text == document_data.text
    assert document.user_id == document_data.user_id
    assert document.conversation_id == document_data.conversation_id
    assert document.url == document_data.url
    assert document.document_id == document_data.document_id
    assert document.message_id == document_data.message_id


def test_get_document(session):
    _ = get_factory("Document", session).create(
        id="1", text="Hello, World!", conversation_id="1", message_id="1"
    )

    document = document_crud.get_document(session, "1")
    assert document.text == "Hello, World!"
    assert document.id == "1"


def test_fail_get_nonexistent_document(session):
    document = document_crud.get_document(session, "123")
    assert document is None


def test_list_documents(session):
    _ = get_factory("Document", session).create(
        text="Hello, World!", conversation_id="1", message_id="1"
    )

    documents = document_crud.get_documents(session)
    assert len(documents) == 1
    assert documents[0].text == "Hello, World!"


def test_list_documents_empty(session):
    documents = document_crud.get_documents(session)
    assert len(documents) == 0


def test_list_documents_with_pagination(session):
    for i in range(10):
        _ = get_factory("Document", session).create(
            text=f"Hello, World! {i}", conversation_id="1", message_id="1"
        )

    documents = document_crud.get_documents(session, offset=5, limit=5)
    assert len(documents) == 5
    for i, document in enumerate(documents):
        assert document.text == f"Hello, World! {i + 5}"


def test_delete_document(session):
    document = get_factory("Document", session).create(
        text="Hello, World!", conversation_id="1", message_id="1"
    )

    document_crud.delete_document(session, document.id)

    document = document_crud.get_document(session, document.id)
    assert document is None
