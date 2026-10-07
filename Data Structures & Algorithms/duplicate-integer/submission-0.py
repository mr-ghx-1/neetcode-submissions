class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = dict.fromkeys(nums, 0)
        print(items)
        return len(items) != len(nums)
        