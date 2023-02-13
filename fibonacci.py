class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fibs = [0] * (n + 1)
            fibs[0] = 0
            fibs[1] = 1
            for i in range(2, n + 1):
                fibs[i] = fibs[i - 1] + fibs[i - 2]
            return fibs[n]
