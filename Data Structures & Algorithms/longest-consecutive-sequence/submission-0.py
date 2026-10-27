class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest = 0 # intialise whats the longest sequence

        for n in nums:
            #Check if its the start of a sequence.
            if (n-1) not in numSet:
                length = 0
                while ( n + length ) in  numSet: #while there is left side 
                    length += 1 #increment it by 1
                longest = max(length,longest) # linearly check 
        return longest
        