class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_pairs(s, pair, score):
            res = 0
            stack = []
            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            return res, "".join(stack)
        
        res = 0
        pair = "ab" if x > y else "ba"
        score = max(x, y)
        min_score = min(x, y)
        
        # Remove pairs with higher score first
        gain, s = remove_pairs(s, pair, score)
        res += gain
        
        # Remove pairs with lower score next
        gain, s = remove_pairs(s, pair[::-1], min_score)
        res += gain
        
        return res

        