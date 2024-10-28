# 283. Move Zeroes - Leetcode


# the approach is to keep track of the first zero found and 
# if a non -zero element is found which is at a position where it's greateer than
# the zero's position then we must swap or simply ignore

# as at example [1, 0, 2], we must swap 2 with 0
# but here [1, 2, 0], we don't have to take care of zero

def findSol(nums) :
    """ actual solutio function """
    numsLen = len(nums)

    # encounter edge case
    if numsLen <= 1 :
        return nums
    
    # -1 indicates that zero isn't found yet
    currFirstZeroIndex = -1
    # keep iterating upto end
    for i in range(numsLen) :
        # set current index of zero if any zero wasn't found earlier
        if (nums[i] == 0) and (currFirstZeroIndex == -1) :
            currFirstZeroIndex = i
            continue
        
        # if an element isn't zero, we've a zero index which is at previous position
        # than the non-zero element then we must swap
        # and also update the current zero index as it's swapped now
        if (nums[i] != 0) and (currFirstZeroIndex != -1) and (currFirstZeroIndex < i) :
            nums[i], nums[currFirstZeroIndex] = nums[currFirstZeroIndex], nums[i]
            currFirstZeroIndex += 1
    
    # return the updated nums
    return nums


# running test cases
print(findSol([0, 1, 0, 3, 12])) #[1, 3, 12, 0, 0]
print(findSol([0])) #[0]
print(findSol([0, 0, -1, -2, 3])) # [-1, -2, 3, 0, 0]
print(findSol([0, 0, 0])) #[0, 0, 0]