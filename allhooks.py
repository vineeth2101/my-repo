II  # example_code.py

# Hook: trailing-whitespace
def example_function():
    print("This function has trailing whitespace.   ")


# Hook: end-of-file-fixer
print("This file does not end with a newline.")

# Hook: check-yaml
yaml_data = """
example:
  - item1
  - item2
  - item3:
      nested_item: value
"""

# Hook: debug-statements
print("This line contains a debug statement: DEBUG_PRINT('Hello')")

# Hook: check-docstring-first
def example_function_with_docstring():
    """This is a docstring."""
    print("Function with docstring.")


# Hook: check-added-large-files
# This file contains a large amount of random data to test the check-added-large-files hook.
large_data = "A" * 1024 * 1024 * 5  # 5 MB

# Hook: check-json
json_data = '{"key": "value", "array": [1, 2, 3], "nested": {"a": 1, "b": 2}}'

# Hook: reorder-python-imports
import os
import sys
from pathlib import Path
from typing import List, Tuple

# Hook: yesqa
def example_type_hinted_function(param: List[Tuple[str, int]]) -> bool:
    return len(param) > 0


# Hook: yamllint
# This line intentionally exceeds the specified line length.
# long_line: This is a very long line that exceeds the recommended line length for testing purposes. This should trigger the yamllint check.

# Hook: black
def example_function_with_black():
    print("This function has not been formatted according to black.")


# Hook: mypy
def example_mypy_function(param: str) -> int:
    return len(param)


# Hook: pylint
# pylint: disable=C0103
variable_with_wrong_name = 42

# Hook: yamlfmt
yaml_data_fmt = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Hook: add-trailing-comma
list_with_trailing_comma = [
    1,
    2,
    3,
]

# Hook: pyupgrade
old_string_format = "This is an old string formatting: %s" % "example"

# Hook: pycln
# This code contains unused imports to test pycln.
import unused_module
from unused_module import unused_function
