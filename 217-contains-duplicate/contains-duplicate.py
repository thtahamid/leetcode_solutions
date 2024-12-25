class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for i in nums:
            if i in n:
                return True
            n.add(i)
        return False
        