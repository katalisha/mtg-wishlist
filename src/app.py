"""Module providingFunction printing python version."""
import sys


def print_python_version():
    print(sys.version)


# this function has a unit test
def python_version():
    return sys.version[:6]


# if the container is running the version will be 3.11.3
print_python_version()


def print_a_thing(thing: str):
    print(thing)


# if the black auto formatter is running, uncommenting the code below and saving
# will change the single quotes to double quotes
print_a_thing("thing 1")
print_a_thing("thing 2")

# if the pyright type checker is working, uncommenting below will show a type
# error
# a: int = 3.5


# if the linter is working, uncommenting below will show a linter error
# def print_a_Big_thing():
# print("🐘")
