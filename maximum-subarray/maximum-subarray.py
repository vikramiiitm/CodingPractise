class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = -99999
        
        for i in range(len(nums)):
            local_max = max(nums[i], local_max+nums[i])
            
            if local_max>global_max:
                global_max = local_max
        return global_max