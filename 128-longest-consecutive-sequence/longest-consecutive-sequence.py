from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = ans = 1

        for i in range(1, len(nums)):
            first, second = nums[i - 1], nums[i]

            if first == second:
                continue                            # skip duplicates

            if first + 1 == second:
                count += 1                          # extend streak
            else:
                count = 1                           # reset streak

            ans = max(ans, count)                   # update best answer

        return ans