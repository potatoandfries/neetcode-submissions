class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+','',s).lower()
        # Remove non-alphanumeric characters and convert to lowercase
        return s == s[::-1]
        