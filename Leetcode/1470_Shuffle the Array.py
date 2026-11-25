class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        x = nums[:n]
        y = nums[n:]
        # zip
        result = []
        for a,b in zip(x,y):
            result.append(a)
            result.append(b)
            # result.extend([a, b])
        return result

        # # 其他寫法
        # for i in range n:
        #     result.append(nums[i])
        #     result.append(nums[i+n])
