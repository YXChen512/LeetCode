class Solution(object):
    def __init__(self):
        self.solution = None

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1
        if last == 0:
            return True
        index = len(nums)-2
        while index>=0:
            if index + nums[index] >= last:
                print('last position brought to %d' % index)
                last = index
            index -= 1
        print('after loop index is %d' % index)
        if last <= 0:
            return True
        else:
            return False

nums = [2,0,1,7]
s = Solution()
s.solution = s.canJump(nums)
print(s.solution)
