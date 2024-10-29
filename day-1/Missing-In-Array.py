# Find The Missing Number - GFG


# approachj is to add all the first n natural numbers
# and the add the elements present in the array

# then to get the missing element subtarct the
# sum of array element from sum of first n elements 

def findSol(arr) :
    """ actual solutin function """

    arrLen = len(arr)

    # encounter edge case
    if arrLen == 0 :
        return 1
    
    # sum of first n
    sumOfFirstN = sum([i for i in range(1, arrLen+2)])

    # sum of array elemets
    sumOfArr = sum([ele for ele in arr])

    # return the subtraction result (the missing element)
    return sumOfFirstN - sumOfArr


# running test cases
print(findSol([1, 2, 3, 5])) #4
print(findSol([8, 2, 4, 5, 3, 7, 1])) #6
print(findSol([1])) #2
print(findSol([])) #1
