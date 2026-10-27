class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        shash = {}
        for i in range(len(nums)):
            seen = target - nums[i]
            if seen in shash:
                return [shash[seen],i]
            else:
                shash[nums[i]] = i
        
            
