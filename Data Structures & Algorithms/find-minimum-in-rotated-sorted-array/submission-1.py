class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left,right = 0 , len(nums) -1

        

        #for i in range(len(nums)): (wrong)
        while left<right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # aka lowest value is right side
                left = mid+1
            else:
                right = mid
        return nums[left]

