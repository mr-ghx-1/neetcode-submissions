class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []

        mul = 1
        for i in range(len(nums)):
            if i > 0:
                mul = mul * nums[i-1]
            pref.append(mul)
        
        mul = 1
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                mul = mul * nums[i+1]
            suff.append(mul)

        suff.reverse()

        result = []

        for i in range(len(nums)):
            result.append(pref[i] * suff[i])

        return result