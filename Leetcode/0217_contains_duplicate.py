class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # if len(nums) == len(set(nums)):
        #     return False
        # return True
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            return False