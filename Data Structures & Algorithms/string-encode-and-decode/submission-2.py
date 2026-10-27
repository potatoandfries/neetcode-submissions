class Solution:

    def encode(self, strs: List[str]) -> str:
        res= ""
        for words in strs:
            res += words+ "0192x"
        return res
    def decode(self, s: str) -> List[str]:
        res = s.split("0192x")[0:-1]
        #res = s.split(" ")[1:] , everything except first.
        return res