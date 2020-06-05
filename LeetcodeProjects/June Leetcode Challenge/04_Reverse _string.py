class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        
        """
        #Convert to string , reverse and convert to list again 
        # result = "".join(s)
        # s = list(str(result[::-1]))
        # print(s)
        #Alternate method 
        
        left,right = 0, len(s)-1
        
        while(left<right):
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1
        #s[len(s)-1] = start
        print(s)
s = Solution()
s.reverseString(["h","e","l","l","o"])