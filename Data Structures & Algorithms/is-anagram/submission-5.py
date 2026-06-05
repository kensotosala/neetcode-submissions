class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        a = list(s)
        b = list(t)
        a.sort()
        b.sort()

        return a == b