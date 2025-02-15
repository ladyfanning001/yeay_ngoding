#input ex : [-2, -1, -3, 4, -1, 2, 1, -5, 4]
#output = 6
#explanation [4, -1, 2, 1]
#subarraynya harus berurutan, terserah isinya berapa tp minimal 1

from typing import List


class Solution:
    def maxSubArray(self, nums : List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums :
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
            
                