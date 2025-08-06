"""
-------------------------------------------
Python file with and without linting error
-------------------------------------------
# Linting Error
def greet(name):
    print(f"Hello, {name}!") # This line has an extra space that violates PEP8
greet("John")

-------------------------------------------
# No Linting Error
def greet(name):
    print(f"Hello, {name}!")


greet("John")
------------------------------------------
"""

def greet(name):
    print(f"Hello, {name}!") # This line has an extra space that violates PEP8
greet("John")
