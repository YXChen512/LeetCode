# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def __init__(self):
        self.solution = None

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        print("number of intervals: %d" % length)
        if length == 0:
            return []
        if length == 1:
            return intervals

        # sort the intervals by their start
        intervals.sort(key = lambda interval:interval.start)
        for interval in intervals:
            print("[%d,%d]" % (interval.start,interval.end))

        #
        mergedIntervals = []
        mergedIntervals.append(intervals[0])
        i = 1
        while i < length:
            current = mergedIntervals[-1]
            print("current interval is [%d,%d]" % (current.start,current.end))
            nextInterval = intervals[i]
            print("next interval is [%d,%d]" % (nextInterval.start,nextInterval.end))
            # current interval includes the nextInterval
            if current.end >= nextInterval.end:
                i += 1
            # if overlap
            elif current.end >= nextInterval.start:
                current.end = nextInterval.end
                i += 1
            # if next completely include nextInterval
            else:
                mergedIntervals.append(nextInterval)
                i += 1
        return mergedIntervals

brackets = [[1,3],[12,16],[8,10],[15,18]]
test = []
for i in range(4):
    test.append(Interval(brackets[i][0],brackets[i][1]))
s = Solution()
s.solution = s.merge(test)
for instant in s.solution:
    print('[%d,%d]' % (instant.start,instant.end))
