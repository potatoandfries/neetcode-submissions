class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

# initial attempt:
#     class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         duppies = []
#         for i in nums:
#             duppies.push(nums[i])
#             nums[i].pop()
#             if nums[i] in duppies:
#                 return nums[i]
# duppies is a list, but you're trying to use push which is not a valid method for lists in Python. Instead, you can use append.
# nums[i].pop() is trying to remove an element from the original list nums, but nums[i] is an integer, not a list. You can't use pop on an integer.
# The logic of the code is not correct. You're trying to find the duplicate by checking if an element is in the duppies list, but you're not correctly updating the duppies list.