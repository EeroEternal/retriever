from retriever.tests.factories.citation import CitationFactory
from retriever.tests.factories.conversation import ConversationFactory
from retriever.tests.factories.document import DocumentFactory
from retriever.tests.factories.file import FileFactory
from retriever.tests.factories.message import MessageFactory
from retriever.tests.factories.user import UserFactory

FACTORY_MAPPING = {
    "User": UserFactory,
    "File": FileFactory,
    "Conversation": ConversationFactory,
    "Citation": CitationFactory,
    "Message": MessageFactory,
    "Document": DocumentFactory,
}


def get_factory(model_name, session=None):
    factory = FACTORY_MAPPING[model_name]
    factory._meta.sqlalchemy_session = session
    return factory
