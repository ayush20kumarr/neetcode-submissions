class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {} #index: value
        for i, ivalue in enumerate(nums):
            diff = target - ivalue
            if diff in hMap:
                return [hMap[diff], i]
            else:
                hMap[ivalue] = i
        return