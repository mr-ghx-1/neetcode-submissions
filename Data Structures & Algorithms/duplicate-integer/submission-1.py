class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = dict.fromkeys(nums, 0)
        return len(items) != len(nums)
        