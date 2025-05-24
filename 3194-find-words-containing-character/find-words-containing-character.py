class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list = []
        n = len(words)
        for i in range(n):
            if x in words[i]:
                list.append(i)
        return list