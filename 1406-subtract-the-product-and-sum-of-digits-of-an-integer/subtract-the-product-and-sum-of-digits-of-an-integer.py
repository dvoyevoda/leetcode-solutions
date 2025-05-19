class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        product_digits = 1
        sum_digits = 0

        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        for d in digits:
            sum_digits += d
            product_digits *= d
        
        return product_digits - sum_digits
        