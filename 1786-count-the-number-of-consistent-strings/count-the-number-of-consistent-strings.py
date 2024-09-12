class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        counter = 0
        for word in words:
            isConsistent = True
            for char in word:
                if char not in allowedSet:
                    isConsistent = False
                    break
            if isConsistent:
                counter += 1
        return counter