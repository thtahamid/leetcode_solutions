class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for w in words:
            if w[:n] == pref:
                count += 1
        return count