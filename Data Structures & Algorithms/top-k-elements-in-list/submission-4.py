class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort (good for known n; bad for streaming)
        count = Counter(nums) #returns num + count
        bucket = [[] for _ in range(len(nums)+1)]

        for n,c in count.items():
            bucket[c].append(n) # append bc list
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) ==k:
                    return res
        