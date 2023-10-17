class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_check = ""
        for i in s:
            if i.lower().isalpha() or i.lower().isdigit():
                s_check += i.lower()

        if s_check == s_check[::-1] or s == " ":
            return True
        return False
