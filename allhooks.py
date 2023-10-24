# Hook: trailing-whitespace
def example_function():
    print("This function has trailing whitespace.        ")


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
