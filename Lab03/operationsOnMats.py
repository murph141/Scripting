#!/usr/local/bin/python3.4

def checkIfMatrixIsValid(matrix):
    """
    Checks if the matrix is valid
    """

    length = 0
    count = 0

    for item in matrix:
        if(type(item) != type([])):
            return(False)

      if(len(item) == 0):
          return(False)

      length += len(item)
      count += 1

    length = length / count

    for item in matrix:
        if(len(item) != length):
            return(False)

    return(True)


def getMatrixSize(matrix):
    """
    Gets the size of the matrix
    """

    check = checkIfMatrixIsValid(matrix)

    if(check == 0):
        return([])

    row = 0
    column = len(matrix[0])

    for item in matrix:
        row += 1

    return([row, column])


def getRow(matrix, rowIndex):
    """
    Gets the row of a given matrix
    """

    check = checkIfMatrixIsValid(matrix)

    if(check == 0):
        return([])

    size = getMatrixSize(matrix)

    if(rowIndex > (size[0] - 1)):
        return([])

    return(matrix[rowIndex])


def getColumn(matrix, columnIndex):
    """
    Gets the column of a given matrix
    """

    check = checkIfMatrixIsValid(matrix)

    if(check == 0):
        return([])

    size = getMatrixSize(matrix)

    if(columnIndex > (size[1] - 1)):
        return([])

    joined = []

    for item in matrix:
        joined.append(item[columnIndex])

    return(joined)


def transposeMatrix(matrix):
    """
    Transposes a given matrix
    """

    check = checkIfMatrixIsValid(matrix)

    if(check == 0):
        return(None)

    [row, col] = getMatrixSize(matrix)

    joined = []
    for i in range(col):
        for item in matrix:
            joined.append(item[i])

    print(joined)
    trans = []
    for i in range(col):
        trans.append(joined[i*row:i*row+row])

    return(trans)

def dotProduct(row, column):
    """
    Gets the dot product of a row and a column vector
    """

    if(len(row) != len(column)):
        return(None)

    if(len(row) == 0 or len(column) == 0):
        return(None)

    sum = 0

    for i in range(len(row)):
        sum += (row[i] * column[i])

    return(sum)


def multiplyMatrices(matrix1, matrix2):
    """
    Multiplies two matrices
    """

    check1 = checkIfMatrixIsValid(matrix1)
    check2 = checkIfMatrixIsValid(matrix2)

    if(check1 == 0 or check2 == 0):
        return(None)

    [row1, col1] = getMatrixSize(matrix1)
    [row2, col2] = getMatrixSize(matrix2)

    if(col1 != row2):
        return(None)

    emptyMatrix = [[0] * col2 for i in range(row1)]

    for i in range(row1):
        for j in range(col2):
            emptyMatrix[i][j] = dotProduct(matrix1[i], transposeMatrix(matrix2)[j])

    return(emptyMatrix)


if __name__ == "__main__":
    pass
