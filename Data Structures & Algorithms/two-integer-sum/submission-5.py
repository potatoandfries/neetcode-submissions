class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # A dictionary to store prev vals.
        result = []  # Store the result here
        for i, n in enumerate(nums):  
            diff = target - n 
            if diff in prevMap:
                result = [prevMap[diff], i]  # Store the result here
            else:
                prevMap[n] = i 
        return result