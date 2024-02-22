
# AA FastAPI Template

A robust and sensible baseline for kick-starting any new FastAPI application, along with optional opinionated development and test dependencies.

## Installation

    # Using pip:
    pip install aa-fastapi-template

    # tests
    ping install aa-fastapi-template[tests]

    # dev
    ping install aa-fastapi-template[dev]

Included within each package are:

| aa-fastapi-template         | aa-fastapi-template[tests]       | aa-fastapi-template[dev]           |
| :---                | :---       | :--- |
| fastapi                    | + aa-fastapi-template         | + aa-fastapi-template[tests] |
| asyncpg              | pytest      | black             |
| environs             | pytest-mock | httpx         |
| uvicorn              | hypothesis  | ruff         |
| mypy                 | pytest-cov  | toml          |
| psycopg2-binary      | pytest-xdist | types-toml        |
| pydantic             | pytest-md   |               |
| python-dotenv        | pytest-emoji |              |
| sqlalchemy           |             |               |
| sqlmodel             |             |               |
