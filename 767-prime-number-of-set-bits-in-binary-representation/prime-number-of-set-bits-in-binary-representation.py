class Solution:
    def binary_prime(self, l:int):
        count=0
        while(l>0):
            if(l%2==1):
                count+=1
            l=int(l/2)
        p_list=[2, 3, 5, 7, 11, 13, 17, 19]
        if(count in p_list):
            return True
        else:
            return False

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            if self.binary_prime(i) == True:
                count+=1

        return count