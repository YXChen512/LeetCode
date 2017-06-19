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
            print("target too small")
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
        print("Current target is:\t%d" % target)
        print("starting index is \t%d" % index)
        # exit condition
        if target == 0:
            print("combination found")
            pool.append(path)
            return
        if target < 0:
            print("negative target %d" % target)
            return
        # depth-first search
        for i in xrange(index,len(candidates)):

            # take care of duplicates:
            if i> index and candidates[i]==candidates[i-1]:
                print("%d duplicates the path: %r" % (candidates[i],path))
                continue

            if target < candidates[i]:
                print("target %d smaller than %d" % (target,candidates[i]))
                return
            else:
                print("keep trying %r" % (path+[candidates[i]]))
                self.dfs(candidates,target - candidates[i],i+1,path + [candidates[i]],pool)


nums = [3,1,1,1,2,2,5,5,7]
s = Solution()
s.solution = s.combinationSum(nums,7)
for combs in s.solution:
    print(combs)
