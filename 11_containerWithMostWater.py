class Solution(object):
    def __init__(self):
        self.solution = None

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mxArea = 0
        i=0
        j= len(height)-1

        while i < j:
            mxArea = max(mxArea,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i +=1
            else:
                j -=1

        return mxArea

s = Solution()
s.solution = s.maxArea([1,0,0,0,9,7,0,0,3,0,0,0,0,0,0,0,0,0])
print(s.solution)
