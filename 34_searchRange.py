class Solution(object):
    def __init__(self):
        self.solution = None

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #corner cases
        if len(nums) == 0:
            return [-1,-1]
        if target < nums[0] or target > nums[-1]:
            return [-1,-1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]
        # binary search
        low, high = 0, len(nums)-1
        anchor = -1 # record the binary search result
        while low < high:
            if target == nums[low]:
                anchor = low
                break
            if target == nums[high]:
                anchor = high
                break
            mid = (low + high)/2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                anchor = mid
                break

        if anchor == -1:
            return [-1,-1]
        else:
            left = right = anchor
            while left > 0 and nums[left] == nums[left - 1]:
                left -= 1
            while right < (len(nums) - 1) and nums[right] == nums[right + 1]:
                right += 1
            return [left,right]

numArray = [5,7,7,8,8,10]
s = Solution()
s.solution = s.searchRange([1],1)
print(s.solution)
