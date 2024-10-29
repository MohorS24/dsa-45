# 566. Reshape The Matrix -Leetcode


# the approach is simple as keep iterating over our input matrix and keep adding 
# the elements to the output matrix, just keep track of the count of current elements of the row 
# and if the row becomes full (according to the input of c), create a new row and keep adding 
# until all the elements are added from the input matrix

def findSol(mat, r, c) :
    """ actual solution function """
    # input matrix row & column
    ipMatRow = len(mat)
    ipMatCol = len(mat[0])

    # encountering edge cases
    if (ipMatCol * ipMatRow) != (r * c) :
        return "reshaping not possible", mat

    if (r == ipMatRow) and (c == ipMatCol) :
        return mat

    # initializing outpout matrix & some other helper variables
    opMat = []
    currRowIndex = -1
    currNoOfEleInRow = 0

    # case if output matrix wants multiple rows
    if r > 1 :
        opMat.append([])
        currRowIndex = 0
    
    # iterating over each element of 2D matrix
    for i in range(ipMatRow) :
        for j in range(ipMatCol) :
            # -1 indicates that output matrix must be of one single row (1D matrix)
            if currRowIndex == -1 :
                opMat.append(mat[i][j])
                continue
            
            # check if we need to skip to the next row of our output matrix 
            if currNoOfEleInRow == c :
                # create a new row & update the row index as the next one
                opMat.append([])
                currRowIndex += 1
                currNoOfEleInRow = 0
            
            # keep adding elements to the output mayrix 
            # and increase the element count of current row after each addition
            opMat[currRowIndex].append(mat[i][j])
            currNoOfEleInRow += 1
    
    # returning the output matrix
    return opMat


# running test cases
print(findSol([[1, 2], [3, 4]], 1, 4)) #[1, 2, 3, 4]
print(findSol([[1, 2], [3, 4]], 2, 2)) #[[1, 2], [3, 4]]
print(findSol([[1, 2], [3, 4]], 4, 1)) #[[1], [2], [3], [4]]
print(findSol([[1, 2, 3], [4, 5, 6]], 3, 2)) #[[1, 2], [3, 4], [5, 6]]
print(findSol([[1, 2], [3, 4]], 2, 8)) #"reshaping not possible", mat