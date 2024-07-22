class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = {}
        for h, n in zip(heights, names):
            pairs[h] = n

        result = []

        for h in reversed(sorted(heights)):
            result.append(pairs[h])
        return result

        