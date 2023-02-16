class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = '({['
        closings = ')}]'
        
        for brack in s:
            if brack in openings:
                stack.append(brack)
            elif brack in closings:
                ind = closings.index(brack)
                if openings[ind] not in stack:
                    return False
                else:
                    if openings[ind] == stack[-1]:
                        stack.pop()
            

        return len(stack) == 0
            
