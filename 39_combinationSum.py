'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
'''

class Solution(object):
    def __init__(self):
        self.solution = None

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        if target < min(candidates):
            return []

        candidates.sort()
        print("the available candidates are:\n %r" % candidates)
        results = []
        self.dfs(candidates,target,0,[],results)
        return results


    def dfs(self,candidates,target, index, path, pool):
        '''
        input:
            candidates, target are the main input
            index: starting position of the current dfs
            path: the former numbers that has been taken
            pool: list of all combinations
        '''
        print("Current path is:\t%r" % path)
        # exit condition
        if target == 0:
            print("combination found")
            pool.append(path)
            return
        # depth-first search
        for i in xrange(index,len(candidates)):
            if target < candidates[i]:
                print("attempt failed")
                return
            else:
                print("keep trying")
                self.dfs(candidates,target - candidates[i],i,path + [candidates[i]],pool)

nums = [2,3,6,7]
s = Solution()
s.solution = s.combinationSum(nums,8)
for combs in s.solution:
    print(combs)
