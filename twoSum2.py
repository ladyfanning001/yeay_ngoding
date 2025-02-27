#sum of two integers in array that is 
# already sorted in ascending order
from typing import List

def twoSum2(self, numbers : List[int], target: int)->List[int]:
    l, r = 0, len(numbers)-1
    
    while l < r:
        curSum = numbers[1] + numbers[r]
        if curSum > target :
            r -= 1
        elif curSum < target :
            l += 1
        else :
            return [l+1, r+1]
    return []