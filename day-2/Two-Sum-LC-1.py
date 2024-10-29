# 1. Two Sum - Leetcode


# keep track of numbers already visited and check 
# if sum with curernt number forms the target

# we can assume that a pair would be present in every input case
# (mentioned in the question)

def findSol(nums, target) :
    """ actual solution function """
    numsLen = len(nums)

    # keep track of numbers found earlier
    numsVisited = {nums[0] : 0}
    
    # keep iterating upto end for finding pair
    for i in range(1, numsLen) :
        # check if current number forms a pair with another among the numbers found earlier
        # then we can return the indices of numbers in pair
        if (target - nums[i]) in numsVisited :
            return [numsVisited[target - nums[i]], i]
        
        # code block if pairing isn't possible yet
        # if current number isn' tin dictionary, add it 
        # (no need to update index of same number)
        if nums[i] not in numsVisited :
            numsVisited[nums[i]] = i


# running test cases
print(findSol([2, 7, 11, 15], 9)) #[0, 1]
print(findSol([3, 2, 4], 6)) #[1, 2]
print(findSol([3, 3], 6)) #[0, 1]
print(findSol([3, 3, 2, 3], 5)) #[0, 2]
