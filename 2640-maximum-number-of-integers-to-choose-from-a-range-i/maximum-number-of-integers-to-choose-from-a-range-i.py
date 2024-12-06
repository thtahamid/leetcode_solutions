class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        arr = set(banned)
        sum = 0
        count = 0
        for i in range(1, n+1):
            if i in arr:
                continue
            sum += i
            
            if sum > maxSum:
                break
            
            count += 1
        return count
        