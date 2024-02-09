#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    return [replace if x == search else x for x in my_list]

# Example usage:
original_list = [1, 2, 3, 2, 4, 2, 5]
search_value = 2
replacement_value = 99

result = search_replace(original_list, search_value, replacement_value)
print(result)
