from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_k = [num for num, count in freq.most_common(k)]

        print(top_k)
        return top_k