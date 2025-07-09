import pytest
from sqlmodel import Session, SQLModel, create_engine

from snipster.models import Snippet

engine = create_engine("sqlite:///:memory:", echo=True)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)


def test_create_snippet():
    snippet = Snippet(
        title="Test Snippet",
        code="print('Hello, World!')",
        description="Test Snippet Description",
        created="Jul-06-2025",
        creator="Karthik G",
    )
    with Session(engine) as session:
        session.add(snippet)
        session.commit()
        session.refresh(snippet)
        assert snippet.id is not None
        assert snippet.title == "Test Snippet"
        assert snippet.code == "print('Hello, World!')"
        assert snippet.description == "Test Snippet Description"
        assert snippet.created == "Jul-06-2025"
        assert snippet.creator == "Karthik G"
