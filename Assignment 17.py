def concat_tuples(tuple1, tuple2):
    """
    Concatenates two tuples and returns the resulting tuple.

    Parameters:
    tuple1 (tuple): The first input tuple.
    tuple2 (tuple): The second input tuple.

    Returns:
    tuple: A new tuple containing all elements from both input tuples.
    """
    return tuple1 + tuple2

# Example usage:
result = concat_tuples((1, 2, 3), (4, 5))
print(result)  # Output: (1, 2, 3, 4, 5)
