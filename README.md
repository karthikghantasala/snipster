# Snipster

python cohort from pybites

# Describe the dir structure

```├── README.md
├── pyproject.toml
├── snipster.db
├── src
│   └── snipster
│   ├── **init**.py
│   ├── **main**.py
│   ├── **pycache**
│   │   ├── **init**.cpython-313.pyc
│   │   └── models.cpython-313.pyc
│   └── models.py
├── tests
│   ├── **init**.py
│   ├── **pycache**
│   │   ├── **init**.cpython-313.pyc
│   │   └── test_model.cpython-313-pytest-8.4.1.pyc
│   └── test_model.py
└── uv.lock
```

# Describe the Application

Application will help capture code snippets and write to database.

# How to Run the Application

uv run python -m src.snipster
uv run python -m src.snipster.models

# How to Run tests

uv run pytest

# UV cheatsheet

curl -LsSf https://astral.sh/uv/install.sh | sh
uv init snipster
uv add ruff
uv add sqlmodel
uv add python-dotenv
uv add --dev poethepoet
uv add --dev pytest-cov
uv run ruff check
uv lock
uv sync
more uv.lock
uv python --list
uv python list

uv run python -m src.snipster
uv tool install pre-commit --with pre-commit-uv
uv list
uv pip list
uv init --package

uv run pytest
uv run python -m src.snipster.models
uv run poe cov
uv tool install poethepoet
