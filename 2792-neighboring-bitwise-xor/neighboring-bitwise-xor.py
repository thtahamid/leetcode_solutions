class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        sum = 0

        for n in derived:
            sum ^= n
        
        return sum == 0