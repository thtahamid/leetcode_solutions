class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for i in count:
          if count[i] > 1:
            return i