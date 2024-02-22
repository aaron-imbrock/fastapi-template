# AA FastAPI Template

A robust and sensible baseline for kick-starting any new FastAPI application. This template provides a comprehensive setup for developing high-performance web applications with FastAPI, including optional, opinionated development and testing dependencies to enhance your development workflow.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

The base package provides the essential tools for creating FastAPI applications. While `[tests]` adds testing libraries, the `[dev]` option installs both testing and development tools.

    # Using pip:
    pip install aa-fastapi-template

    # tests
    pip install aa-fastapi-template[tests]

    # dev
    pip install aa-fastapi-template[dev]

## Package Options

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

## Contributing

We welcome contributions to the AA FastAPI Template! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

- Issues: Use the [GitHub Issues page](https://github.com/aaron-imbrock/aa-fastapi-template/issues)
- Pull Requests: Submit pull requests with your changes/fixes.
