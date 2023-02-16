class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        low = 0
        high = len(nums) - 1
        count = 0

        while low < high:
            total = nums[low] + nums[high]
            if total == k:
                low += 1
                high -= 1
                count += 1
            elif total > k:
                high -= 1
            else:
                low += 1

        return count
