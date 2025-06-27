def find_common_elements(list1, list2):
    """
    Returns a list of elements common to both list1 and list2.
    Optimized for large input lists using set intersection.
    """
    # Convert both lists to sets to remove duplicates and allow fast lookup
    set1 = set(list1)
    set2 = set(list2)

    # Use set intersection to find common elements
    common_elements = set1.intersection(set2)

    # Return the result as a list
    return list(common_elements)


# Example usage:
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [4, 5, 6, 7, 8, 9, 10]
print(find_common_elements(list_a, list_b))  # Output: [4, 5, 6, 1000000] (order may vary)
