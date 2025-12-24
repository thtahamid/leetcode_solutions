class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        boxes = 0
        while total_apples > 0:
            total_apples -= capacity[boxes]
            boxes += 1

        return boxes