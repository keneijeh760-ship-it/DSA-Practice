class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(num):
            index[num] = i

        for i, num in enumerate(num):
            diff = target-num
            if diff in index adn index[diff] != i:
                return [i, index[diff]]
        return []