class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.solution = None

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # if list is longer than k,
        # reverse the first k nodes
        #call itself for the next group
        # else,return head

        # corner case: k == 0 or 1
        if k < 2:
            return head

        # check if longer than k
        if head is None:
            print("length of list mod k is 0")
            return head
#        print("before reverse: %d %d %d" % (head.val,head.next.val,head.next.next.val))
        pointer = head
        step = 0
        print("checking if the length of list is larger or equal to k")
        while pointer.next and step < k-1:
            print("now step is %d" % step)
            print("node value is %d" % pointer.val)
            pointer = pointer.next
            step +=1
        print("now step is %d" % step)
        print("node value is %d" % pointer.val)
        if step == k - 1:
            # pointer is now at the k_th node
            #========reverse the first k nodes=====
            cap = ListNode(0)
            cap.next = head
#            print("cap and head are: %d, %d" % (cap.val,cap.next.val))
            end = pointer # end stick to the k_th node
            print("the end of this k-group is %d" % end.val)
            tail = head # after the reverse, the current head will be the tail

            pointer = pointer.next # indicates the head of the next group
            if pointer:
                print("the next k-group startes with %d" % pointer.val)
            else:
                print("There is no next group")

            while cap.next is not end:
#                print("before reverse: %d %d %d" %
#                    (cap.next.val,cap.next.next.val,cap.next.next.next.val))
                # cut head node loose and put it next to end
                cap.next = head.next
                head.next = end.next
                end.next = head
                print("end node and its next node: %d, %d" % (end.val,end.next.val))
#                print("after reverse: %d %d %d" %
#                    (cap.next.val,cap.next.next.val,cap.next.next.next.val))
                # target on the new head node
                head = cap.next
                print("the new head is %d" % head.val)
            #========= first k nodes reversed ==============
            print("the head of the reversed group: %d" % cap.next.val)
            print("the end of the reversed k-group is %d" % tail.val)
            if pointer is None:
                return cap.next
            else:
                tail.next = self.reverseKGroup(pointer,k)
                return cap.next
        else:
            print("the last group is not complete and not reversed")
            return head

testList1 = ListNode(-10)
testList1.next = ListNode(-6)
testList1.next.next = ListNode(7)
tail= testList1.next.next
tail.next = ListNode(3)
tail = tail.next
tail.next = ListNode(4)
tail = tail.next
tail.next = ListNode(9)
tail = tail.next



s = Solution()
s.solution = s.reverseKGroup(testList1,2)
alist = s. solution
while alist:
    print alist.val
    alist = alist.next
