from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def countmajor(arr, num, left, right):
            count = 0
            for i in range(left, right + 1):
                if arr[i] == num:
                    count += 1
            return count

        def mej(arr, left, right):
            if left == right:
                return arr[left]
            
            mid = (left + right) // 2
            leftMajor = mej(arr, left, mid)
            rightMajor = mej(arr, mid + 1, right)

            if leftMajor == rightMajor:
                return leftMajor

            leftcount = countmajor(arr, leftMajor, left, right)
            rightcount = countmajor(arr, rightMajor, left, right)

            return leftMajor if leftcount > rightcount else rightMajor

        return mej(nums, 0, len(nums) - 1)
