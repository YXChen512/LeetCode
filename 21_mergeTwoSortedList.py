# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def insertNode(singular, main, reverseOrder = False):
    '''
    _insertNode() is an internal function called by Solution class's mergeTwoLists method
    Insert a singular node into the main sorted linked list
    The length of main is larger than 2
    The main list is changed
    Two return values: head node of the new main list, and the downstream node of the singular node after insertion
    '''
    if reverseOrder:
        # descending
        if singular.val >= main.val:
            singular.next = main
            return singular,main
        else:
            pointer = main
            while pointer.next and singular.val < pointer.next.val:
                pointer = pointer.next
            # if while loop stopped in the middle of the main
            if pointer.next:
                downstream = pointer.next
                pointer.next = singular
                singular.next = downstream
                return main,downstream
            else:
                # pointer has moved to the end of main list
                pointer.next = singular
                return main,None
    else:
        # ascending order
        if singular.val <= main.val:
            singular.next = main
            return singular,main
        else:
            pointer = main
            while pointer.next and singular.val > pointer.next.val:
                pointer = pointer.next
                # if while loop stopped in the middle of the main
            if pointer.next:
                downstream = pointer.next
                pointer.next = singular
                singular.next = downstream
                return main,downstream
            else:
                pointer.next = singular
                return main,None



class Solution(object):
    def insertNode(self, node, list, reversed = False):
        '''
        Insert the node into the sorted linked list according to the given order
        Default order is ascending
        '''

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        # default order is ascending order
        # when both lengths are 1, put in ascending order
        # but when either is longer than 1, the actual order has to be figured out first
        # by default the two lists are in the same order, both ascending or descending
        """
        if l1 is None and l2 is None:
            return []
        if l1 is None and l2:
            return l2
        if l2 is None and l1:
            return l1

        if l1.next is None and l2.next is None:
            if l1.val < l2.val:
                l1.next = l2
                return l1
            else:
                l2.next = l1
                return l2
        elif l1.next is not None and l2.next is not None:
            # both are actually lists
            # check the orders of l1 and l2
            # since both lists are ordered
            # the inserted position is helpful for future insertation

            # check order of l1
            pointer1 = l1
            while pointer1.next and pointer1.val == pointer1.next.val:
                # find the non-equal nodes to see the order
                pointer1 = pointer1.next
            if pointer1.next:
                descending1 = (pointer1.val > pointer1.next.val)
                while pointer1.next:
                    pointer1 = pointer1.next
                # now pointer1 is the tail of l1
            else:
                # which mease all nodes have the same value
                descending1 = False
            # check order of l2
            pointer2 = l2
            while pointer2.next and pointer2.val == pointer2.next.val:
                pointer2 = pointer2.next
            if pointer2.next:
                descending2 = (pointer2.val > pointer2.next.val)
                while pointer2.next:
                    pointer2 = pointer2.next
                # now pointer2 is the tail of l2
            else:
                #  which mease all nodes have the same value
                descending2 = False

            # if both are the same order
            if descending1 == descending2:
                order = descending1
                # simple cases when l1 and l2 can be connected head-to-tail
                if order == True:
                    if pointer1.val > l2.val:
                        pointer1.next = l2
                        return l1
                    if pointer2.val > l1.val:
                        pointer2.next = l1
                        return l2
                else:
                    #order == False, ascending
                    if pointer1.val < l2.val:
                        pointer1.next = l2
                        return l1
                    if pointer2.val < l1.val:
                        pointer2.next = l1
                        return l2

                # repeatedly take the head of l2 and insert it into l1
                # before doing that, an initial step needs to be done to set variables for the while loop
                # namely, headnode, downstream,
                headnode = l2
                l2 = l2.next
                l1, downstream = insertNode(headnode,l1,order)
                tempTail = headnode

                while l2.next and downstream:
                    headnode = l2
                    l2 = l2.next
                    HEAD, downstream = insertNode(headnode,downstream,order)
                    tempTail.next = HEAD
                    tempTail = headnode

                # now either l2.next is None, or downstream is None
                if downstream is None:
                    # tempTail is the end of l1, so no downstream
                    tempTail.next = l2
                else:
                    # l2 has only one node left, but cannot be put to the tail of l1
                    HEAD, downstream = insertNode(l2,downstream,order)
                    tempTail.next = HEAD
                return l1


            else:
                print("The two lists do not have the same order!")
                return None
                """
                # ascending one is the base, descending one is the feed
                # recursively take off the head of the feed and insert it in the base
                if descending1:
                    base = l2
                    feed = l1
                else:
                    base = l1
                    feed = l2
                # recursively take the head of the descending list into the ascending list
                # the current headnode is smaller than the previous one
                # so it's going to be btw the base and the previous one
                headnode = feed
                feed = feed.next
                HEAD, downstream = insertNode(headnode,base,order)
                base = HEAD
                newInsert = headnode
                while feed.next and downstream:
                    headnode = feed
                    feed = feed.next
                    HEAD, downstream = insertNode(headnode,base,order)
                    newInsert.next = HEAD
                # now either feed.next is None, or downstream is None
                if downstream is None:
                    newInsert.next = feed
                else:
                    # feed has only one node left, but cannot be put to the tail of l1
                    base, downstream = insertNode(feed,base,order)
                return base
                """

        else:
            # either l1 or l2 has only one item
            if l1.next is None:
                singular = l1
                main = l2
            else:
                singular = l2
                main = l1
            pointer = main
            while pointer.next and pointer.val == pointer.next.val:
                pointer = pointer.next
            if pointer.next:
                descending = (pointer.val > pointer.next.val)
            else:
                descending = False
            head, downstream = insertNode(singular,main,descending)
            return head

testList1 = ListNode(-10)
testList1.next = ListNode(-6)
tailpointer = testList1.next
tailpointer.next = ListNode(-5)
tailpointer =tailpointer.next
tailpointer.next = ListNode(-5)
tailpointer =tailpointer.next

testList2 = ListNode(-4)
testList2.next = ListNode(-3)
tailpointer = testList2.next
tailpointer.next = ListNode(-2)
tailpointer =tailpointer.next
tailpointer.next = ListNode(-1)
tailpointer =tailpointer.next
tailpointer.next = ListNode(1)
tailpointer =tailpointer.next
tailpointer.next = ListNode(7)
tailpointer =tailpointer.next

s = Solution()
s.solution = s.mergeTwoLists(testList1,testList2)
testList = s.solution
while testList:
    print testList.val
    testList = testList.next
#testList, tailpointer = insertNode(ListNode(3),testList)
