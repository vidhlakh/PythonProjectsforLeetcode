class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        # j iterate through subsequence wh iterate through whole string 
        j,wh =0,0 
        while wh <len(t):
            if s[j] == t[wh]:
                j +=1 
            wh += 1
            if j == len(s):
                return True
        return False





s = Solution()
print(s.isSubsequence("aec","abcde"))