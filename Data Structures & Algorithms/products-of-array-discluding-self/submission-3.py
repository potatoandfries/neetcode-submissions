class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
            ## prefix[1]= prefix[0]*nums[0] =1*1=1
            # prefix[2] = prefix[1]*2=2
            # prefix [3] = prefix[2]*4 =8 which is correct
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]* nums[i+1]
        
        return [prefix[i]* suffix[i]for i in range(n)]
