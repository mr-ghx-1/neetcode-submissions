class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if (i - 1) in num_set:
                continue

            cur = i
            while cur in num_set:
                cur += 1
            
            longest = max(cur - i, longest)
        
        return longest