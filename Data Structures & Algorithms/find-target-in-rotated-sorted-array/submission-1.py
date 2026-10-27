class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                # rotation point is to the right of mid
                # => left..mid is the SORTED half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1      # target is in sorted left half
                else:
                    left = mid + 1       # target must be in right half
            else:
                # nums[mid] < nums[right]
                # => mid..right is the SORTED half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1       # target is in sorted right half
                else:
                    right = mid - 1      # target must be in left half

        return -1