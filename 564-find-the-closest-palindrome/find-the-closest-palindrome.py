class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # Edge case: for numbers like 1, return 0
        if n == "1":
            return "0"
        
        # First candidate: '9' followed by length-1 nines (like '999...999')
        candidates.add(str(10 ** (length - 1) - 1))
        
        # Second candidate: '1' followed by length-1 zeros and ending with '1' (like '100...001')
        candidates.add(str(10 ** length + 1))
        
        # Main candidates: modify the first half of n
        prefix = int(n[:(length + 1) // 2])
        
        # Generate three possible palindromes by modifying the first half
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(candidate)
        
        # Remove n itself from the candidates
        candidates.discard(n)
        
        # Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome

# Example usage:
# sol = Solution()
# print(sol.nearestPalindromic("123"))  # Output: "121"
# print(sol.nearestPalindromic("1"))    # Output: "0"
       