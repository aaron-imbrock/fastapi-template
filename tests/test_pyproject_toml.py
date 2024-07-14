import pytest
import toml
from typing import Any, Dict

# Path to your pyproject.toml
PYPROJECT_TOML_PATH = "pyproject.toml"


def load_pyproject_toml() -> Dict[str, Any]:
    """
    Utility function to load the pyproject.toml file.
    """
    with open(PYPROJECT_TOML_PATH) as toml_file:
        return toml.load(toml_file)


def test_toml_syntax() -> None:
    """
    Test if the pyproject.toml file has valid syntax by attempting to load it.
    This test checks toml syntax not pyproject.toml syntax.
    """
    try:
        pyproject_content = load_pyproject_toml()
        assert pyproject_content is not None
    except toml.TomlDecodeError:
        pytest.fail("pyproject.toml contains invalid TOML syntax.")


def test_pyproject_toml_contains_project_section() -> None:
    """
    Test if the pyproject.toml file contains a [project] section.
    """
    pyproject_content = load_pyproject_toml()
    assert (
        "project" in pyproject_content
    ), "pyproject.toml must contain a [project] section."


def test_pyproject_toml_project_name() -> None:
    """Test if the pyproject.toml file specifies a project name under [project]."""
    pyproject_content = load_pyproject_toml()
    assert (
        "name" in pyproject_content["project"]
    ), "The [project] section must specify a name."
