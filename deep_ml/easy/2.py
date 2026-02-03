def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    a_transposed = [[] for i in range(len(a[0]))]
    for line in a:
        for index, value in enumerate(line):
            a_transposed[index].append(value)

    return a_transposed
