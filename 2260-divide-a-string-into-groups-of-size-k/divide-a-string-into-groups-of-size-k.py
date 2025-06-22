class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i+k])
        if len(res[-1]) < k :
            res[-1] = res[-1].ljust(k, fill) # in built python function "ljust" fills the missing character by justifying from the left
        return res