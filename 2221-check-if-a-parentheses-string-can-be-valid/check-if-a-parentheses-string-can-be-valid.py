class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack_locked = []
        stack_unlocked = []
        
        for i in range(len(s)):
            if locked[i] == "0":
                stack_unlocked.append(i)
            elif s[i] == "(":
                stack_locked.append(i)
            else:
                if stack_locked:
                    stack_locked.pop()
                elif stack_unlocked:
                    stack_unlocked.pop()
                else:
                    return False
        
        while stack_locked and stack_unlocked and stack_locked[-1] < stack_unlocked[-1]:
            stack_locked.pop()
            stack_unlocked.pop()

        if stack_locked:
            return False

        return True



        