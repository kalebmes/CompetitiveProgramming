class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            start, end = l[i], r[i]
            subarray = nums[start:end+1]
            counter = Counter(subarray)
            if len(counter) < 2:
                res.append(True)
            else:
                sortedSubarray = sorted(subarray)
                diff = sortedSubarray[1] - sortedSubarray[0]
                isArithmetic = True
                for j in range(2, len(sortedSubarray)):
                    if sortedSubarray[j] - sortedSubarray[j-1] != diff:
                        isArithmetic = False
                        break
                res.append(isArithmetic)
        return res
