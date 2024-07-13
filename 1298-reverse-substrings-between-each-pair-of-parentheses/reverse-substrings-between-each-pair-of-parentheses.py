class Solution(object):
    def reverseParentheses(self, s):
        # neetcode
        stack = []
        for c in s:
            if c == ")":
                myString = []
                while stack[-1] != "(":
                    myString.append(stack.pop())
                stack.pop()
                stack.extend(myString)
            else:
                stack.append(c)
        return "".join(stack)


        # stack = []
        # for char in s:
        #     if char == ')':
        #         rev = ""
        #         while stack and stack[-1] != '(':
        #             rev += stack.pop()
        #         if stack:
        #             stack.pop()  # pop the opening bracket
        #         for c in rev:
        #             stack.append(c)
        #     else:
        #         stack.append(char)

        # return ''.join(stack)
        """
        :type s: str
        :rtype: str
        """
        
        