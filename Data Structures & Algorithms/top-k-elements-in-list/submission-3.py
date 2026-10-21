class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        result = []

        for i in range(k):
            high = None
            for j in freq:
                if j in result:
                    continue
                if high == None or freq[j] > freq[high]:
                    high = j
            result.append(high)

        return result