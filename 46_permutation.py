class Solution(object):
    def __init__(self):
        self.solution = None

    def dfs(self,permutations,incomplete,nums):
        if len(incomplete)==len(nums):
            permutations.append(incomplete)
            print('new permutation found: %r' % incomplete)
            print('total amount of permutations saved: %d' % len(permutations))
            return
        for number in nums:
            if number not in incomplete:
                #print('put %d into the incomplete permutation: %d' % (number,incomplete))
                self.dfs(permutations, incomplete + [number],nums)


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is []:
            return []

        if len(nums)==1:
            return [nums]
        else:
            results = []
            #
            self.dfs(results,[],nums)
        return results

nums = [2,3,6,7]
s = Solution()
s.solution = s.permute(nums)
for perm in s.solution:
    print(perm)
