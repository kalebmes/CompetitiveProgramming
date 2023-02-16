class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        
        return -heapq.heappop(heap) if heap else 0
