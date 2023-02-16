class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Use a min-heap to keep track of the k most frequent elements
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        
        # Return the k most frequent elements
        return [num for freq, num in heap]
