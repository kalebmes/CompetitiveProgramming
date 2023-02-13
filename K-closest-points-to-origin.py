class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        heapq.heapify(answer)
        for point in points:
            d = point[0]**2 + point[1]**2
            heapq.heappush(answer, (-d, point))
            if len(answer) > k:
                heapq.heappop(answer)

        return [y for x, y in answer]
