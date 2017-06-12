# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.solution = None

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        bottom = head
        i = n
        while i > 0 and bottom.next:
            bottom = bottom.next
            print("Bottom pointer moved down")
            i -= 1
        print("bottom indicator i is %d" % i)
        # when the Nth from end is the head
        if i==1:
            print("%d_th node from end is the head" % n)
            return head.next
        # when the Nth is not the head, add an upstream pointer
        elif i == 0:
            upstream = head
        else:
            print("%d exceeds the length of list" % n)
            return None

        while bottom.next:
            upstream = upstream.next
            bottom = bottom.next
        upstream.next = upstream.next.next
        return head

testList = ListNode(0)
testList.next = ListNode(2)
tailpointer = testList.next
tailpointer.next = ListNode(5)

s = Solution()
s.solution = s.removeNthFromEnd(testList, 4)
#print(testList.next.val)
testList = s.solution
while testList:
    print testList.val
    testList = testList.next
