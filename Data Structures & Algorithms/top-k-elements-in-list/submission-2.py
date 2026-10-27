class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)#have to use freq.items() bc u cant sort a dict direclty
        
        return [x[0] for x in sorted_freq[:k]] ##up to not including kth value so k number of values. k-1 index.]