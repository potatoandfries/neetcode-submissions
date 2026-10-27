class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        shash, thash = {}, {}
        for c in s:
            shash[c] = shash.get(c, 0) + 1
        for c in t:
            thash[c] = thash.get(c, 0) + 1
        return shash == thash
        # this is legit soln ;
        