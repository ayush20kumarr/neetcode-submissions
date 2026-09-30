class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        count1 = 0

        candidate2 = None
        count2 = 0

        # Phase1: find the candidte

        for x in nums:
            if x == candidate1:
                count1 = count1 + 1
            elif x == candidate2:
                count2 = count2 + 1
            elif count1 == 0:
                candidate1 = x
                count1 = 1
            elif count2 == 0:
                candidate2 = x
                count2 = 1
            else:
                count1 = count1 - 1
                count2 = count2 - 1

        # Phase2: Verification
        c1 = 0
        c2 = 0

        for x in nums:
            if x == candidate1:
                c1 = c1 + 1
            elif x == candidate2:
                c2 = c2 + 1
        
        # Phase3: Result

        res = []
        limit = len(nums) // 3
        if c1 > limit:
            res.append(candidate1)
        if c2 > limit:
            res.append(candidate2)
        return res
            