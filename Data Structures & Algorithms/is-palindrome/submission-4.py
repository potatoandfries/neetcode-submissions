# ============================================================
# MISTAKES IN ORIGINAL CODE:
# ============================================================
# 1. `s[left].isalnum.lower()` is WRONG.
#    - `isalnum` and `lower` are two separate methods.
#    - Must call them separately: `s[left].isalnum()` and `s[left].lower()`.
#    - Writing `isalnum.lower()` returns a bound method object, which is
#      always truthy -> the condition never behaves as intended.
#
# 2. INFINITE LOOP: using `continue` after finding a valid alphanumeric
#    character without advancing the pointer. If s[left] IS alphanumeric,
#    `continue` restarts the loop without moving `left`, so it loops forever.
#
# 3. LOGIC ORDER: compared characters BEFORE confirming both pointers
#    landed on alphanumeric characters. Must skip non-alphanumeric first,
#    then compare.
#
# 4. BOUNDS SAFETY: inner pointer movement didn't guard against
#    `left < right`, risking IndexError and comparing beyond valid range.
#
# 5. STRUCTURE: using top-level `if/else` for skipping is messy; nested
#    `while` loops express "skip all non-alphanumerics" more clearly.
# ============================================================

# ============================================================
# IDEAL SOLUTION (Two Pointers, O(n) time, O(1) space)
# ============================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left<right and not s[left].isalnum():
                left+=1

            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase versions
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    testcase = "this siht"
    print(sol.isPalindrome(testcase))
