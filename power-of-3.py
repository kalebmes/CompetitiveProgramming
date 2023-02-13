if n == 1:
        return True
    if n < 3:
        return False
    return isPowerOfThree(n / 3)
