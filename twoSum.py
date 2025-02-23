#given an array of integers, return incides
#of the two numbers sucj that they add up to specific target

#ex : [2, 7, 11, 15], target = 9
#output : [0, 1]

def twoSum(self, nums: list[int], target : int) -> list[int]:
    prevMap = {} #val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap :
            return [prevMap[diff], i]
        prevMap[n] = i
        return [] #if no such pair found

    