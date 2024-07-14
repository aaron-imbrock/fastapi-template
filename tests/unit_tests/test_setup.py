import subprocess
import sys
import pytest
import os
from typing import List

def test_install_package() -> None:
    """Test if the package can be installed using pip."""
    result = subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".[testing]"], capture_output=True, text=True)
    assert result.returncode == 0, f"Installation failed: {result.stderr}"

def test_dependencies() -> None:
    """Test if all dependencies are installed correctly."""
    result = subprocess.run([sys.executable, "-m", "pip", "check"], capture_output=True, text=True)
    assert result.returncode == 0, f"Dependencies check failed: {result.stderr}"

def test_metadata() -> None:
    """Test if the package metadata is correct."""
    result = subprocess.run([sys.executable, "setup.py", "--name"], capture_output=True, text=True)
    assert result.returncode == 0, f"Metadata check failed: {result.stderr}"
    assert result.stdout.strip() == "aa-fastapi-template", "Package name is incorrect"

def test_package_contents() -> None:
    """Test if the package contains the expected files."""
    expected_files: List[str] = ["pyproject.toml", "setup.py", "LICENSE"]
    for file in expected_files:
        assert os.path.exists(file), f"Expected file {file} is missing"

if __name__ == "__main__":
    pytest.main([__file__])
