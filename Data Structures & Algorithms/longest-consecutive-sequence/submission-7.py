class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        values = {num: 1 for num in nums}
        lowest = min(values.keys())
        highest = max(values.keys())
        # print(values)
        # print(lowest, highest)

        counter = 0
        max_counter = 0
        for i in values.keys():
            if i-1 in values:
                continue

            nex = i
            while True:
                if nex in values:
                    counter += 1
                    nex += 1
                else: 
                    break
            max_counter = max(counter, max_counter)
            counter = 0
        
        return max_counter