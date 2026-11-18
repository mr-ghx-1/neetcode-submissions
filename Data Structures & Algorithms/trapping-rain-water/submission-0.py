class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        r = []

        lmax, rmax = (0, 0)
        for i in range(0, len(height)):
            l.append(max(height[i], lmax))
            if lmax < height[i]:
                lmax = height[i]
        for i in range(len(height)-1, -1, -1):
            r.append(max(height[i], rmax))
            if rmax < height[i]:
                rmax = height[i]
        r.reverse()

        fill = 0
        for i in range(0, len(height)):
            fill += min(l[i], r[i]) - height[i]
        
        return fill