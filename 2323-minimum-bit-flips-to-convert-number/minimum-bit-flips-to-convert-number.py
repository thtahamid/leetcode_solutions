class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        ans = 0
        
        while xor_result > 0:
            ans += xor_result & 1  
            xor_result >>= 1     
        
        return ans
        