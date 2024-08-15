class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for x in bills:
            if x == 5:
                five += 1
            if x == 10:
                ten += 1

            change = x - 5 
            if change == 5:
                if five > 0:
                    five -= 1
                else: 
                    return False
            if change == 15:
                if five and ten :
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five -= 3
                else: 
                    return False

        return True

        # five = 0
        # ten = 0
        # if bills[0] != 5:
        #     return False

        # else:
        #     for x in bills:
        #         if x == 5:
        #             five += 1
        #         elif x == 10:
        #             if five > 1 :
        #                 five -= 1
        #                 ten += 1
        #             else:
        #                 return False
        #         elif x == 20:
        #             if five > 1 and ten >1 :
        #                 five -= 1
        #                 ten -=1 
        #             elif ten < 1 and five > 2 :
        #                 five -= 3
                        
                


