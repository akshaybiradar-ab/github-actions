"""
--------------------------------------------
Python file with and without linting error
--------------------------------------------
# Linting Error
def greet(name):
    print(f"Hello, {name}!") # This line has an extra space that violates PEP8
greet("John")

# Workflow Error
Run flake8 python/
python/script.py:20:1: E302 expected 2 blank lines, found 1
python/script.py:21:29: E261 at least two spaces before inline comment
python/script.py:22:1: E305 expected 2 blank lines after class or function definition, found 0
Error: Process completed with exit code 1.

-------------------------------------------
# No Linting Error
def greet(name):
    print(f"Hello, {name}!")


greet("John")
------------------------------------------
"""

def greet(name):
    print(f"Hello, {name}!")


greet("John")
