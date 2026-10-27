class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for s in strs:
            s_sorted = tuple(sorted(s))  # convert to tuple because lists can't be dictionary keys
            if s_sorted not in anagram:
                anagram[s_sorted] = [s]  # create new list with s as the first element
            else:
                anagram[s_sorted].append(s)  # append s to the existing list
        return list(anagram.values())
