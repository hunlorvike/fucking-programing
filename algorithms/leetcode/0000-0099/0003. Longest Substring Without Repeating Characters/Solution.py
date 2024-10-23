class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        answer = start = 0
        for index, char in enumerate(s):
            while char in subString:
                subString.remove(s[start])
                start += 1
            subString.add(char)
            answer = max(answer, index - start + 1)
        return answer
