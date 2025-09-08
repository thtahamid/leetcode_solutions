class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

      # def check(x):
      #   return '0' not in str(x)

      for a in range(1, n):
        b = n - a
        # if check(a) and check(b):
        if "0" not in str(a) and "0" not in str(b):
          return [a, b]
