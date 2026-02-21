class Solution:
    
    def is_prime_set_bits(self, n: int) -> bool:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return n.bit_count() in primes

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        
        for i in range(left, right + 1):
            if self.is_prime_set_bits(i):
                count += 1
        
        return count