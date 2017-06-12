class Solution(object):
    def __init__(self):
        self.solution = None

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]:
            all the UNIQUE combination of three numbers in nums,
            which make the sum equal to zero
        """
        if nums is None:
            #print("Input is None")
            return []
        if len(nums)<3:
            #print("Input list doest NOT have three elements!")
            return []

        results =[]
        nums.sort()
        for i in xrange(len(nums)-2):
            if i==0 or (nums[i] != nums[i-1]):
                left,right = i+1, len(nums)-1
                while left < right:
                    sumOfThree = nums[i] + nums[left] + nums[right]
                    if sumOfThree == 0:
                        results.append([nums[i], nums[left], nums[right]])
                        while left < len(nums)-1 and nums[left]==nums[left + 1]:
                            left +=1
                        while right > i+1 and nums[right]== nums[right -1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sumOfThree < 0:
                        while left < len(nums)-1 and nums[left]==nums[left + 1]:
                            left +=1
                        left +=1
                    else:
                        while right > i+1 and nums[right]== nums[right -1]:
                            right -= 1
                        right -=1

        return results



s = Solution()
s.solution = s.threeSum([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(s.solution)
