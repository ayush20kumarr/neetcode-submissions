class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {} # value : freq

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i]+=1
        for freq in hmap.values():
            if freq > 1:
                return True
        return False
