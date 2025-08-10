class Solution:
    # Please Read Approach for easier Understanding
    def reorderedPowerOf2(self, n: int) -> bool:
        powers=[]
        for i in range(30):
            powers.append(2**i)
        n=str(n)
        l=len(n)
        possible=[]
        real_count=defaultdict(int)
        check_count=defaultdict(int)
        for i in range(l):
            real_count[n[i]]+=1
        for power in powers:
            if len(str(power))==l:
                possible.append(power)
        for power in possible:
            check_count=defaultdict(int)
            power=str(power)
            for i in range(len(power)):
                check_count[power[i]]+=1
            if check_count==real_count:
                return True
        return False
            

        

        