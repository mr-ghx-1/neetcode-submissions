class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        num_set = set(nums)
        max_counter = 0

        for i in num_set:
            if (i - 1) in num_set:
                continue

            cur = i
            while cur in num_set:
                cur += 1
            
            max_counter = max(cur - i, max_counter)
        
        return max_counter