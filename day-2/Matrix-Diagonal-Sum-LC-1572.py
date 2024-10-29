# 1572. Matrix Diagonal Sum - Leetcode


# approach is to kepp adding all diagonal elments present in each row, 
# we'll add the values from 2 rows at same step as we'll be approaching 
# from both upper & lower side of matrix at each step

# and just add the element at center of matrix at first
# if umber of rows are odd in number as it's the only
# element that's present as single in a row in the whole matrix

def findSol(mat) :
    """ actual solution function """

    row = len(mat)

    # initial value of diagonal sum
    diagSum = 0
    # add the element at center of matrix
    # if number of rows and columns are odd in number
    if row % 2 == 1 :
        diagSum += mat[row // 2][row // 2]
    
    # iterate upto the row before middle row of matrix 
    # and keep adding diagonal elements present in current row
    # & it's mirror row from lower side
    for i in range(row // 2) :
        diagSum += ( mat[i][i] + mat[i][(row-1) - i] + 
                    mat[(row-1) - i][i] + mat[(row - 1) - i][(row - 1) - i] )
    
    # return the final diagonal sum
    return diagSum


# running test cases
print(findSol([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) #25
print(findSol([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])) #8
print(findSol([[5]])) #5
