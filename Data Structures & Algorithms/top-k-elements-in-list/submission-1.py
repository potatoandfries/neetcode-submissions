class Solution:
    ## My soln
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the dictionary by value (frequency) in descending order
            #.items() returns the tuple as a list
            # key=lambda x: x[1] , this means that you take x as a value and return the 1st index
            # reverse means descending not ascending
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Return the top k frequent elements
        #sorted_freq[:k]] give me first k th element.
        #[x[0] for x in...]: This is a list comprehension that extracts the first element of each tuple in the slice.
        #In other words, it extracts the keys (elements) from the tuples.
    return [x[0] for x in sorted_freq[:k]]