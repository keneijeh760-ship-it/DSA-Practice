class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            Tsum = numbers[l] + numbers[r]

            if Tsum < target:
                l += 1
            elif Tsum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return []
        
