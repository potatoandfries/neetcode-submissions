class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #this returns length of word :> blackbox to see why
            i = j + 1 # this will point first letter of the orginal string 
            j = i + length # this will poin to the end of the word+1
            res.append(s[i:j])#  starting index (inclusive), ending index (exclusive)
            i = j
            
        return res
