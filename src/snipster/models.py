import os

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()


class Snippet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str


if __name__ == "__main__":
    DB_HOST = os.environ["DB_HOST"]
    engine = create_engine(f"sqlite:///{DB_HOST}")
    SQLModel.metadata.create_all(engine)
    print("Database + table created!")
