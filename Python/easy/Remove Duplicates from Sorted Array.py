class Solution:
    def removeDuplicates(self, nums) -> int:
        nums = sorted(list(set(nums)))
        return len(nums)