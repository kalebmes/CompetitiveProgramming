class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        for s in range(len(nums) - 1, -1, -1):
            for e in range(s, len(nums)):
                if s == e:
                    dp[s][e] = nums[s]
                else:
                    a = nums[s] - dp[s + 1][e]
                    b = nums[e] - dp[s][e - 1]
                    dp[s][e] = max(a, b)
        return dp[0][len(nums) - 1] >= 0
