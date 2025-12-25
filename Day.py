class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_len =1
        curr_len = 1
        new = sorted(set(nums))

        for i in range(1, len(new)):
            if new[i] == new[i-1] + 1:
                curr_len +=1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
        return max_len

        
