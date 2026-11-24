class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count = 0
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count > max_count:
                max_count = word_count

        return max_count
#     return max(len(s.split()) for s in sentences)
# 可以一行解決 用max函數
# return max(s.count(' ') + 1 for s in sentences)
# 利用題目保證單字跟單字之間只有一個空格 空格加一就是單字數 取max