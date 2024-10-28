# 344. Reverse String - Leetcode


# we're not using the one liner string reverse approach [::-1], 
# the approach will be to reach upto the position jiust before middle of string (list)
# and swap every element with it's mirror one from the end side

def findSol(s) :
    """ actual solution function """

    strLen = len(s)

    # encountering edge cases
    if strLen == 1 :
        return s
    elif strLen == 2 :
        s[0], s[1] = s[1], s[0]
        return s

    # iterate upto the element just before the middle one
    for i in range((strLen//2) + 1) :
        # swap the current one with mirror element from end
        s[i], s[strLen - (i+1)] = s[strLen - (i+1)], s[i]
    
    return s


# running test cases
print(findSol(["h", "e", "l", "l", "o"])) #["o", "l", "l", "e", "h"]
print(findSol(["h", "a", "n", "n", "a", "h"])) #["h", "a", "n", "n", "a", "h"]
print(findSol(["x", "y"])) #["y", "x"]