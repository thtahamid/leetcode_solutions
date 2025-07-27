class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        unique = []
        for num in nums:
            if not unique or unique[-1] != num:
                unique.append(num)

        if len(unique) < 3:
            return 0

        count = 0
        for i in range(1, len(unique) - 1):
            if unique[i] > unique[i - 1] and unique[i] > unique[i + 1]:
                count += 1
            elif unique[i] < unique[i - 1] and unique[i] < unique[i + 1]:
                count += 1

        return count