import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select

from .models import Snippet

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]


class SnipsterRepo(ABC):
    @abstractmethod
    def add_snippet(self, snippet: Snippet) -> None:
        pass

    @abstractmethod
    def delete_snippet(self, id: int) -> None:
        pass

    @abstractmethod
    def list_snippets(self) -> list | None:
        pass

    @abstractmethod
    def get_snippet(self, id: int) -> Snippet | None:
        pass


# InMemorySnippetRepo is a placeholder for a repository that handles in-memory storage of snippets.
# it  implements methods to add, delete, list, and get snippets from memory.
class InMemorySnippetRepo(SnipsterRepo):
    def __init__(self) -> None:
        self._data: dict[int, Snippet] = {}

    def add_snippet(self, snippet: Snippet) -> None:
        next_id = max(self._data.keys(), default=0) + 1
        self._data[next_id] = snippet

    def list_snippets(self) -> list[Snippet]:
        return list(self._data.values())

    def get_snippet(self, snippet_id: int) -> Snippet | None:
        return self._data.get(snippet_id)

    def delete_snippet(self, snippet_id: int) -> None:
        self._data.pop(snippet_id, None)


#     def add_snippet(self, Snippet):
#         return super().add_snippet(snippet)


class DatabaseSnippetRepo(SnipsterRepo):
    def __init__(self, database_url: str | None):
        self.engine = create_engine(os.environ["DATABASE_URL"])

    #    DbClass(url...

    def add_snippet(self, Snippet):
        # new_snippet = Snippet(title="Test Snippet",
        # code="print('Hello, World!')",
        # description="Test Snippet Description",
        # created="Jul-06-2025",
        # creator="Karthik G")
        with Session(self.engine) as session:
            session.add(Snippet)
            session.commit()
        print("Snippet added successfully!")

    def list_snippets(self):
        with Session(self.engine) as session:
            statement = select(Snippet)
            results = session.exec(statement)
            return results.all()

    def get_snippet(self, id: int):
        with Session(self.engine) as session:
            statement = select(Snippet).where(Snippet.id == id)
            results = session.exec(statement)
            if results:
                return results.first()
            else:
                print("Snippet not found.")

    def delete_snippet(self, id: int) -> None:
        with Session(self.engine) as session:
            statement = select(Snippet).where(Snippet.id == id)
            results = session.exec(statement)
            snippet = results.first()
            if snippet:
                session.delete(snippet)
                session.commit()
                print(f"Snippet with id {id} deleted successfully!")
            else:
                print(f"No snippet found with id {id}.")


# JSONSnippetRepo is a placeholder for a repository that handles JSON formatted snippets.
# It  implements methods to add, delete, list, and get snippets in JSON format.
class JSONSnippetRepo(SnipsterRepo):
    pass


# def main() -> None:
#     repo = DatabaseSnippetRepo()
#     repo.add_snippet(
#         Snippet(
#             title="Test Snippet",
#             code="print('Hello, USA!')",
#             description="Test Snippet Description",
#             created="Jul-06-2025",
#             creator="Karthik G",
#         )
#     )
#     print("Snippet added successfully!")

#     snippets = repo.list_snippets()
#     if snippets:
#         print("List of Snippets:")
#         for snippet in snippets:
#             print(
#                 f"Title: {snippet.title}, Code: {snippet.code}, Description: {snippet.description}, Created: {snippet.created}, Creator: {snippet.creator}"
#             )
#     else:
#         print("No snippets found.")

#     get_snippet = repo.get_snippet(1)
#     if get_snippet:
#         print(
#             f"Snippet Found: {get_snippet.title}, Code: {get_snippet.code}, Description: {get_snippet.description}, Created: {get_snippet.created}, Creator: {get_snippet.creator}"
#         )
#     else:
#         print("Snippet not found.")

#     repo.delete_snippet(1)


# if __name__ == "__main__":
#     main()
