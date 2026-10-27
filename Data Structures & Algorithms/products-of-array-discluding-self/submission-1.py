class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            # update prefix value with current value to make it a prefix.
            #leftest num is always 1*
    
            prefix *= nums[i]
        
        postfix = 1 
        # for i in range(len(nums):0:-1) #starts at rightest value , not include 0
        for i in range(len(nums)-1,-1,-1): #starts 1 after rightest value includes 0
            res[i] *= postfix
            postfix *= nums[i]
        return res
        