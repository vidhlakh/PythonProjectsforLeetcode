import math
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     logValue = math.log2(n)
    #     if logValue.is_integer():
    #         return True
    #     return False


    #O(log n ) time complexity
    # def isPowerOfTwo(self, n: int) -> bool:
    #     while(n%2 ==0):
    #         n = n/2
    #     return n==1

    #O(1) time complexity 
    #Binary value of 1,2,4,8,64.. will have only one 1
    # def isPowerOfTwo(self, n: int) -> bool:
    #     print(bin(n).count('1'))
    #     if bin(n).count('1') ==1 and n>=1:
    #         return True
    #     return False
    # n&(-n )
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: 
            return False
        return n & (-n) == n 

s = Solution()
print(s.isPowerOfTwo(218))
print(s.isPowerOfTwo(-64))


# Power of Two 
# 1,2,4,8,16,32,64,
