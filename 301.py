# Given a string s that contains parentheses and letters, remove 
# the minimum number of invalid parentheses to make the input string valid.
# Return all the possible results. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]

# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]

# Example 3:
# Input: s = ")("
# Output: [""]

from typing import List
class Solution:
    def solve(self, expression: str, mra: int, ans: List[str]) -> List[str]:
        if mra == 0:
            mrnow = self.getMin(expression)
            if mrnow == 0:
                if expression not in ans:
                    ans.append(expression)
            return

        for i in range(len(expression)):
            left = expression[:i]
            right = expression[i+1:]
            self.solve(left+right, mra-1, ans)

    def getMin(self, expression: str) -> int:
        stack = []
        for i in range(len(expression)):
            if expression[i] == '(':
                stack.append(expression[i])
            elif expression[i] == ')':
                if len(stack) is not 0 and stack[-1] == '(':
                    stack.pop()
                elif len(stack) == 0 or stack[-1] == ')':
                    stack.append(')')
        return len(stack)


    def removeInvalidParentheses(self, s: str) -> List[str]:
        minRemoval = self.getMin(s)
        ans = []
        self.solve(s, minRemoval, ans)
        return ans

s = Solution()
expression = "(a)())()"
result = s.removeInvalidParentheses(expression)
print(result)
        