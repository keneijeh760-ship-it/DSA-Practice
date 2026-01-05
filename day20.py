class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        for i in range(len(nums) - k + 1):
            maxVal = nums[i]
            for j in range(i, k + i):
                maxVal = max(maxVal, nums[j])
            res.append(maxVal)
        return res
        
