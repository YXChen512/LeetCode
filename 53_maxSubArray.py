class Solution(object):
    def __init__(self):
        self.solution = None

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        # Solve a sub problem: the max sum of a subArray ending with index i
        # Store S(i) for each index
        # return the max among all the S(i)

        solutions = []
        # S(0) = nums[0] itself
        solutions.append(nums[0])
        print(solutions)

        for index in range(1,len(nums)):
            if solutions[index-1] > 0:
                solutions.append(nums[index] + solutions[index - 1])
            else:
                solutions.append(nums[index])
            print(solutions)
        return max(solutions)



s = Solution()
s.solution = s.maxSubArray(nums)
print(s.solution)
v1, v2 = [2,4],[1,3]
m = [v1,v2]
print(m[0][0])
