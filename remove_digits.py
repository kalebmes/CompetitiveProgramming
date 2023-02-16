class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining digits if k > 0
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # If result is empty, return "0"
        if not result:
            return "0"
        
        return result
