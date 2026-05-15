class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(nums):
            result = target - value
            if result in hashmap:
                return [hashmap[result], i]
            else:
                hashmap[value] = i
        return
