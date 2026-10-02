class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxi = nums[0]

        for i in range(len(nums)):
            #Step 1: Add the current element to the running sum
            summ = summ + nums[i]
            #Step 2: Update the maximum subarray sum found so far
            maxi = max(maxi, summ)
            #Step 3: Discard the current subarray if its sum becomes negative
            if summ < 0:
                summ = 0
        return maxi
