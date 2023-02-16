class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n, 1, -1):
            idx = arr.index(max(arr[:i]))
            if idx != i-1:
                if idx != 0:
                    res.append(idx+1)
                    arr[:idx+1] = reversed(arr[:idx+1])
                res.append(i)
                arr[:i] = reversed(arr[:i])
        return res
