class Solution:
    def factors(self, n):    
        return [[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0]
    def closestDivisors(self, num: int) -> List[int]:
        factors = self.factors(num+1)
        factors.extend(self.factors(num+2))
        f1,f2 = factors[0]
        for x,y in factors:
            if abs(x-y) < abs(f1-f2):
                f1,f2 = x,y
        return [f1,f2]
