class Solution(object):
    def majorityElement(self, nums):
        unique_nums = set(nums) 
        
        for n in unique_nums:
            if nums.count(n) > len(nums) // 2:
                return n
