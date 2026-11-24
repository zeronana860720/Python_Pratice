class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# 不用split 的解法
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()             # 先去掉尾巴的空格
        count = 0
        for c in reversed(s):      # 從最後一個字元往前看
            if c == ' ':           # 碰到空格，代表最後一個單字結束了
                break
            count += 1
        return count