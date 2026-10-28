class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heapq solution // good for Stream questions ; not ideal for prod;
        #prod just use # return [num for num, _ in Counter(nums).most_common(k)]
        counter = Counter(nums)
        heap = []

        for val,freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(freq,val)) #just add value into it
            else:
                heapq.heappushpop(heap,(freq,val)) #add and return lowest freq.
            
        return [h[1] for h in heap] # h in heap; h is tuple with [freq, val] since u only want val;h[1]

        # Time : O(n *log (k) ) // Space : O(n+k)