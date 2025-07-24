import pytest

from snipster.models import Snippet
from snipster.repo import InMemorySnippetRepo


@pytest.fixture(scope="function")
def repo():
    return InMemorySnippetRepo()


@pytest.fixture(scope="function")
def add_snippet_1(repo):
    snippet = Snippet(
        title="Test Snippet",
        code="print('Hello, Test!')",
        description="An example snippet for testing.",
        created="Jul-21-2025",
        creator="Test User",
    )
    repo.add_snippet(snippet)
    return snippet


def test_add_snippet(repo, add_snippet_1):
    assert repo._data[1] == add_snippet_1


def test_list_snippets(add_snippet_1, repo):
    assert repo._data[1] == add_snippet_1
    assert len(repo.list_snippets()) == 1


def test_get_snippet(add_snippet_1, repo):
    assert repo.get_snippet(1) == add_snippet_1


def test_delete_snippet(add_snippet_1, repo):
    repo.delete_snippet(1)
    assert repo._data.get(1) is None
