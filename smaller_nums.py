class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numlist = [0] * 101
        for x in nums:
            numlist[x] += 1
        
        for i in range(1, len(numlist)):
            numlist[i] += numlist[i-1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = numlist[nums[i]-1]
        
        return res
