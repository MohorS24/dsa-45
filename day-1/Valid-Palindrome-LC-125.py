# 125. Valid Palindrome - Leetcode


# the approach is to create a list of valid and lower case characters from string
# and then check the elements one by one with their corresponding 
# reverse elements in the list for the validity for being a palindrome

# we're crafting a list first as it would be easier to check one by one if they're all valid characters now

def findSol(s) :
    """ actual solution function """
    # encounter edge case
    if len(s) <= 1 :
        return True
    
    # crafting valid list of all lower case characters 
    sValidCharList = [ch.lower() for ch in s if ch.isalnum()]

    # x pointer will start from index 0
    # and y pointer will come from the last index
    x, y = 0, len(sValidCharList) - 1
    
    # iterate until two pointers meet each other
    while(x < y) :
        # checking validity at each step
        if sValidCharList[x] != sValidCharList[y] :
            return False
        
        # update pointers for next step
        x += 1
        y -= 1
    
    # at this point it's a valid string
    # as if wasn't it would return false earlier
    # so we can return true
    return True


# running test cases
print(findSol("A man, a plan, a canal: Panama")) #True
print(findSol("race a car")) #False
print(findSol(" ")) #True