class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums.copy()
        # 不能直接寫 ans = nums：= 只是讓 ans 指向同一個 list，不會複製
        # 這樣 append 到 ans 也等於 append 到 nums，邊走訪邊變長 → 無限迴圈
        # 要用 nums.copy() 做出一份獨立的 list
        # ans = list(nums)  # 用 nums 建一個新的 list
        # ans = nums[:]  # 切片：從頭切到尾，會產生新的 list
        for n in nums:
            ans.append(n)
        return ans