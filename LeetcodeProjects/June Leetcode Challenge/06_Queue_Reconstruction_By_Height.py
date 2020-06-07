import math
class Solution:
    #Sorting with desc order of height 
    # if height is same , arrange in order of k
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        result =[]
        for p in people:
            result.insert(p[1],p)
        return result

s = Solution()
print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))