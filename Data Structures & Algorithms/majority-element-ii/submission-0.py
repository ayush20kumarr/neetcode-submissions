class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        me2_limit = len(nums) // 3

        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > me2_limit and x not in result:
                result.append(x)
        return result