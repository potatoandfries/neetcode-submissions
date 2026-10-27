class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if  len(nums) - len(set(nums)) >= 1:
            return True
        else:
            return False