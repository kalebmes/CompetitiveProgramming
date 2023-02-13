class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numlist = [int(x) for x in nums]
        numlist.sort()
        n = len(nums)
        return str(numlist[n-k])
