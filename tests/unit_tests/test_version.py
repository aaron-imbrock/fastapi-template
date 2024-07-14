from typing import Tuple, Union

def test_version_types() -> None:
    # Import the version variables from the target file
    import fastapi_template._version as version_module

    # Ensure the types are correctly inferred
    assert isinstance(version_module.__version__, str)
    assert isinstance(version_module.__version_tuple__, tuple)
    assert isinstance(version_module.version, str)
    assert isinstance(version_module.version_tuple, tuple)

    # Check the types of the elements in the version tuple
    for element in version_module.__version_tuple__:
        assert isinstance(element, (int, str))

def test_type_checking_variable() -> None:
    import fastapi_template._version as version_module

    # Ensure TYPE_CHECKING variable is correctly set
    assert isinstance(version_module.TYPE_CHECKING, bool)
    assert version_module.TYPE_CHECKING is False
