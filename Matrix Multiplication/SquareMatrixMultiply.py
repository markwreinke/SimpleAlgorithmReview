# A simple algorithm to compute the multiplcation of two square matrices of the same size
# The procedure takes Theta(n^3) time because of the triply-nested for loops.

import Matrix

def squareMatrixMultiply(matrixA, matrixB):
    if(matrixA.numRows != matrixA.numColumns or matrixA.numRows != matrixB.numRows or matrixA.numRows != matrixB.numColumns):
        raise NotApplicableError("Matrices must be the square matrices of the same size")

    n = matrixA.numRows
    matrixC = matrixA
    for i in range(0, n):
        for j in range (0,n):
            matrixC.editMatrix(i,j,0)
            for k in range(0, n):
                matrixC.editMatrix(i,j, matrixC.getElement(i,j) + matrixA.getElement(i,j)*matrixB.getElement(i,j))

    return matrixC
