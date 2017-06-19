# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.solution = None

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cap = ListNode(0)
        cap.next = head
        end = cap

        nextpair = head

        while nextpair:
            if nextpair.next is None:
                return cap.next
            else:
                first = nextpair
                second = nextpair.next
                nextpair = second.next

                end.next = second
                second.next = first
                first.next = nextpair

                end = first
        if nextpair is None:
            return cap.next
