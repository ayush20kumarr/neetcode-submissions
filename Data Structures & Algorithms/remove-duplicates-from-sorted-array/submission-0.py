class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if (len(nums)) == 0:
            return -1
        
        k = 1

        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]: #check for unique
                nums[k] = nums[x]   # place unique element
                k +=1
        return k