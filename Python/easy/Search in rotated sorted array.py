class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(target in nums):
            return nums.index(target)
            # for i in range(len(nums)):
            #     if(nums[i]==target):
            #         return i
            #     else:
            #         continue
        else:
            return -1
        
