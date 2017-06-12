# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def Digitize(self):
        # Exceptions
        if self.val < 0:
            print("Input is NOT non-negative")
            return None
        if type(self.val) is not int:
            print("Input is NOT an integer")
            return None

        remainder = self.val

        root = ListNode(remainder)
        lastDigit = root
        while remainder is not 0:
            if remainder/10 == 0:
                return root
            lastDigit.val = remainder % 10
            remainder = remainder / 10
            lastDigit.next = ListNode(remainder)
            lastDigit = lastDigit.next

    def ListItems(self):
        pointer = self
        items = []
        while pointer is not None:
            items.append(pointer.val)
            pointer = pointer.next
        return items

def Length(node):
        if node is None:
            print("ListNode Object does NOT exist!!")
            return 0
        l=0
        pointer = node
        while pointer is not None:
            l += 1
            pointer = pointer.next
        return l

def getNumber(node):
        if node is None:
            return 0
        else:
            return node.val + 10 * getNumber(node.next)

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # check Input
    # case 1, both None
    if l1 is None and l2 is None:
        print("Cannot have both Null inputs")
        return None

    if l1 is not None:
        digits = l1.ListItems()
        if sum([type(x)!= int for x in digits]):
            print("There is NON-integer node(s)!!")
        # check if every node of l1 has single digit
        if sum([x/10>0 for x in digits])>0:
            print("l1 contains multi-digital numbers")
            return None
        if l2 is None:
            return l1

    if l2 is not None:
        digits = l2.ListItems()
        if sum([type(x)!= int for x in digits]):
            print("There is NON-integer node(s)!!")
        if sum([x/10>0 for x in digits])>0:
            print("l2 contains multi-digital numbers")
            return None
        if l1 is None:
            return l2

    # Now l1, l2 are both good
    pointer1 = l1
    pointer2 = l2
    carry = 0
    root = pointer3 = ListNode(0)
    while pointer1 or pointer2 or carry:
        if pointer1:
            carry += pointer1.val
            pointer1 = pointer1.next
        if pointer2:
            carry += pointer2.val
            pointer2 = pointer2.next
        carry, val = divmod(carry,10)
        pointer3.next = ListNode(val)
        pointer3 = pointer3.next
    return root.next

    #
number1 = ListNode(9993).Digitize()
number2 = ListNode(9).Digitize()
#print(Length(number1))
number3 = addTwoNumbers(number1,number2)
print(number3.ListItems())
print(getNumber(number3))
