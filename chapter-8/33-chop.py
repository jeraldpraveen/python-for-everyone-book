def chop(list_values):
    """Removes the first and last elements from a list.

    Args:
        list_values (list): The list from which to remove the first and last elements.

    Returns:
        list: The modified list with the first and last elements removed.
    """
    if len(list_values) <= 2:
        return []
    return list_values[1:-1]


# Example usage:
original_list = [1, 2, 3, 4, 5]
modified_list = chop(original_list)
print("Original list:", original_list)
print("Modified list:", modified_list)

# Output:
# Original list: [1, 2, 3, 4, 5]
# Modified list: [2, 3, 4]"""Removes the first and last elements from a list."""
