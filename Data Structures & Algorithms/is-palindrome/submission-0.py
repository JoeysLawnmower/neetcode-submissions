class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s).lower()
        print(s)
        i = 0
        j = len(s) - 1
        for c in s:
            if c == s[j]:
                j-=1
                print(c, "c", s[j], "j")
            else:
                return False
        return True
