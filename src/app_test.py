"""
Test app methods
"""

from app import python_version


def test_print_python_version():
    assert python_version() == "3.11.3"
