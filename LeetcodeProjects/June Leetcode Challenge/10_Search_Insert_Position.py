class Solution:
    def searchInsert(self, nums, target) :
        if len(nums) == 0:
            nums.append(target)
        if target in nums:
            return nums.index(target)
        else:
            wholeListIsLess = False
            for i, num in enumerate(nums):
                if num > target:
                    break
                if i == len(nums)-1:
                    wholeListIsLess = True
            if wholeListIsLess:
                i = i+1
            nums.insert(i,target)
            return i
        
    #Binary search method 
    # def searchInsert(self, nums, target) :
    #     start = 0
    #     end = len(nums) - 1

    #     while start <= end:
    #         mid = (start + end) // 2
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] > target:
    #         end = mid - 1
    #     else:
    #         start = mid + 1
    #     return start

s = Solution()
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1], 0))
print(s.searchInsert([], 0))