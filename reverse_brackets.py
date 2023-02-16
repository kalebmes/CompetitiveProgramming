class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = ""
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                temp = ""
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                for i in range(len(temp)):
                    stack.append(temp[i])
        
        while stack:
            result += stack.pop()
        
        return result[::-1]
