import random


# Implement matrix multiplication using python
def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B using dynamic programming (Strassen's algorithm).
    Assumes A and B are valid matrices with compatible dimensions.
    Returns the resulting matrix C = A * B.
    """
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if matrix dimensions are compatible for multiplication
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions are not compatible for multiplication.")

    # Initialize the result matrix C with zeros
    C = [[0] * cols_B for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


if __name__ == "__main__":
    # Example usage
    cols_A, rows_A = map(
        int, input("Enter rows and column size for matrix A: ").split(" ")
    )
    cols_B, rows_B = map(
        int, input("Enter rows and column size for matrix B: ").split(" ")
    )
    A = [[random.randint(1, 10) for _ in range(cols_A)] for _ in range(rows_A)]
    B = [[random.randint(1, 10) for _ in range(cols_B)] for _ in range(rows_B)]

    print("Matrix A:")
    for row in A:
        print(row)

    print("Matrix B:")
    for row in B:
        print(row)

    result = matrix_multiply(A, B)
    for row in result:
        print(row)
