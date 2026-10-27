class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = sorted(nums)
        for i in range(len(newList)-1):
            # everything except last if newlist =3
            # range (2) 0,1 exclduing 2 so everything but last*
            if newList[i] == newList[i+1]:
                return True
        return False

         