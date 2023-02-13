class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        count_dict = {}
        for n in nums:
            if n in count_dict:
                count += count_dict[n]
                count_dict[n] += 1
            else:
                count_dict[n] = 1
        return count
