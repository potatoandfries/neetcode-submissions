class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                i = num
                current_streak = 1

                while i+1 in num_set:
                    i += 1
                    current_streak += 1
##The reason is that num is not being updated in the while loop.
## You're checking if num + 1 is in the set, but you're not incrementing num itself.
##This means that the while loop will run indefinitely, because num never changes.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak