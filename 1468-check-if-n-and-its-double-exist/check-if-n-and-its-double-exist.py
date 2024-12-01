class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        my_set = set()
        for i in arr:
            if i*2 in my_set or i/2 in my_set:
                return True
            else:
                my_set.add(i)
        return False