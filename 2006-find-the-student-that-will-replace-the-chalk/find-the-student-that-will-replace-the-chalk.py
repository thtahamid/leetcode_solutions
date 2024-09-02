class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        n_chalk = sum(chalk)

        remainder = k % n_chalk

        n_chalk_used = 0
        for i in range(len(chalk)):

            n_chalk_used += chalk[i] 

            if n_chalk_used > remainder:
                
                return i

                  