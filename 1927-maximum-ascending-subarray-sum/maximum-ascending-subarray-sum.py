class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            # curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
            if nums[i] > nums[i-1]:
                curr = curr + nums[i]
            else:
                curr = nums[i]
            ans = max(ans, curr)
        return ans