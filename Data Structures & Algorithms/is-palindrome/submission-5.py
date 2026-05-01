class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""

        for i in range(len(s)):
            if s[i].isalnum():
                s1 += s[i].lower()

        return s1 == s1[::-1]