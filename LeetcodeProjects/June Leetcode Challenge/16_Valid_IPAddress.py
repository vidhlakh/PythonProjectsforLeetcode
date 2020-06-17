#Look at https://leetcode.com/problems/validate-ip-address/
import re
class Solution:
    # def validIPAddress(self, IP: str) -> str:
    #     try:
    #         socket.inet_aton(IP)
    #         print("This is valid IP address") 
    #     except:
    #         print("This is invalid IP address")
    def validIPAddress(self, IP: str) -> str:
        
        if re.search('^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$',IP): 
            return 'IPv4'
        elif re.search('^([\da-f]{1,4}:){7}[\da-f]{1,4}$',IP,re.I): 
            return 'IPv6'
        else: 
            return 'Neither'
            
        

s = Solution()
s.validIPAddress("172.16.254.9")
s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
s.validIPAddress("256.256.256.256")