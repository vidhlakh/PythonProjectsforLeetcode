class Solution:

    #Sorting with constant colors 
    def sortColors(self, nums):
        left = 0
        cur =0
        right = len(nums)-1
        while cur<=right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right] ,nums[cur]
                right -= 1
            else:
                cur += 1
s = Solution()
s.sortColors([2,0,2,1,1,0])