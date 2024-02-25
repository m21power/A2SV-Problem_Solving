class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MODULO = 10**9 + 7 
        def my_pow(base, exponent):
            result = 1
            while exponent > 0:
                
                if exponent % 2 == 1:
                    result = (result * base) % MODULO
                # Square the base and reduce the exponent by half.
                base = (base * base) % MODULO
                exponent //= 2
            return result
        return (my_pow(5, (n + 1) // 2) * my_pow(4, n // 2)) % MODULO
