class Solution:
    def twoSum(self, nums, target):
        
        for index,val in enumerate(nums):
            nums[index] = None
            if target-val in nums[index:]:
                return [index,nums.index(target-val)]
        
s = Solution() 
nums = [3,3]
k =s.twoSum(nums,6)  
print(k)
                
        