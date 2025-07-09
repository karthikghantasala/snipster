import os

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()


class Snippet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str
    description: str
    created: str
    creator: str


if __name__ == "__main__":
    DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(f"sqlite:///{DATABASE_URL}")
    SQLModel.metadata.create_all(engine)
    print("Database + table created!")
