import Matrix

def squareMatrixMultRecursive(matrixA, matrixB):
    if(matrixA.numRows != matrixA.numColumns or matrixA.numRows != matrixB.numRows or matrixA.numRows != matrixB.numColumns):
        raise NotApplicableError("Matrices must be the square matrices of the same size")

    n = matrixA.numRows
    matrixC = matrixA
    if n == 1:
        matrixC.editMatrix(0, 0, matrixA.getElement(0,0)*matrixB.getElement(0,0))

    else:
        ## TODO:
        pass;

        ''' This is where we divide each matix into n/2 by n/2 matrices,
        in which C00 = recursive(A00, B00) + recursive(A01,B10), C01 = recursive(A00, B01) + recursive(A01, B11)....etc. '''

    return matrixC
