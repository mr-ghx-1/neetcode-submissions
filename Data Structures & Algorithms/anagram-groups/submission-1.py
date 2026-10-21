class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = dict()
        for i in strs:
            y = tuple(sorted(i))
            if y in x:
                x[y].append(i)
            else:
                x[y] = [i]
        
        result = []
        for j in x:
            result.append(x[j])
        
        return result
