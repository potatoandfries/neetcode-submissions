class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {} 
        for i in strs:
            i_sorted = tuple(sorted(i))
            if i_sorted in anagram:
                anagram[i_sorted].append(i)
            else:
                anagram[i_sorted] = [i]  # Initialize with a list containing the string
                #if you dont do this you cant append shit inside.
        return list(anagram.values())