class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}") # f-string new stuff, An f-string is a string literal prefixed with f (or F) that lets you embed Python expressions directly inside { }. At runtime, Python evaluates each {...} and substitutes the result into the string.
        return "".join(parts)          
        
        

            #mistake
            #res.join(str(len(s))+"#"+s) #.join does not mutate it returns new
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            start = j+1
            res.append(s[start:length+start])
            i=length+start
        return res