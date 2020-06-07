#Dynamic Programming table 
#For example [1,2] , try the amount with 2 only 
#then try the amount with 1 and 2 . If amount is 5, 5-2=3 , reuse calculated value for 3 and add 

# 		Column – amount								
# 		0	1	2	3	4	5	6	7	8
# 	Row Coin 0	1	0	0	0	0	0	0	0	0
# 	1	1	1	1	1	1	1	1	1	1
# try doing 2 only , then 2 and 1	1,2	1	1	2	2	3	3	4	4	5

class Solution:
    def change(self, amount, coins) :
        dp =[0]*(amount+1)
        dp[0] =1
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] += dp[x - coin]
        return dp[amount]


s = Solution()
print(s.change(5,[1,2,5]))