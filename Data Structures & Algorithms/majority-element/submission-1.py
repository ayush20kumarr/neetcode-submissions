class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Phase1:
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count = count + 1
            else:
                count = count - 1
        # Phase 2:

        count = 0

        for x in nums:
            if x == candidate:
                count = count + 1

        if count > len(nums) // 2:
            return candidate
        return None
