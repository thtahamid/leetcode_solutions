class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        len_part = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= len_part and ''.join(stack[-len_part:]) == part:
                del(stack[-len_part:])
        return ''.join(stack)