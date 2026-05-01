class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew=""
        for i in s:
            if i.isalnum():
                snew=snew+i.lower()

        return snew==snew[::-1]
        