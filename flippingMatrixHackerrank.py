def flippingMatrix(matrix):
    n = len(matrix)//2
    arr = []
    for i in range(n):
        for j in range(n):
            temp = []
            temp.append(matrix[i][j])
            temp.append(matrix[i][2*n-j-1])
            temp.append(matrix[2*n-i-1][j])
            temp.append(matrix[2*n-i-1][2*n-j-1])
            arr.append(max(temp))

    return sum(arr)

# Example usage:


if __name__ == '__main__':
    # Input matrix
    input_matrix = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108]
    ]

    # Output result
    output = flippingMatrix(input_matrix)
    print(output)
