from docutils.nodes import target


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #
    # 用dict解
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
            # 沒找到的時候 記下自己