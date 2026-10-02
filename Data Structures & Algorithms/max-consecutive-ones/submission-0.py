class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        current_One = 0
        for x in nums:
            if x == 1:
                current_One +=1
                maxOnes = max(maxOnes, current_One)
            else:
                current_One = 0
        return maxOnes

