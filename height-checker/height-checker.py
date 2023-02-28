class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        no_match = 0
        sorted_heights = sorted(heights)
        for i, height in enumerate(heights):
            if heights[i] != sorted_heights[i]:
                no_match += 1
        return no_match
        