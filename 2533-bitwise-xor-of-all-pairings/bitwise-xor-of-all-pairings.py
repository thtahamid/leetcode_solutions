class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        # odd and even length
        nums3 = 0

        if len(nums2) % 2 == 1 :
            for n in nums1:
                nums3 ^= n
        if len(nums1) % 2 == 1:
            for n in nums2 :
                nums3 ^= n
        return nums3
