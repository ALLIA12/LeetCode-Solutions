# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 != None and l2 != None:
        carry = 0
        head = None
        tail = None
        while l1 != None and l2 != None:
            tempSum = l1.val + l2.val + carry
            newVal = tempSum % 10
            carry = tempSum // 10
            l1 = l1.next
            l2 = l2.next
            if head == None:
                head = ListNode(newVal, None)
                tail = head
            else:
                tail.next = ListNode(newVal, None)
                tail = tail.next
    # Check if first one is empty and second isn't:
    if l1 == None and l2 != None:
        while l2 != None:
            tempSum = l2.val + carry
            newVal = tempSum % 10
            carry = tempSum // 10
            l2 = l2.next
            tail.next = ListNode(newVal, None)
            tail = tail.next
    # Check if second one is empty and first isn't:
    if l1 != None and l2 == None:
        while l1 != None:
            tempSum = l1.val + carry
            newVal = tempSum % 10
            carry = tempSum // 10
            l1 = l1.next
            tail.next = ListNode(newVal, None)
            tail = tail.next
    if carry != 0:
        tail.next = ListNode(carry, None)
    return head


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Creating the linked lists
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])

temp = addTwoNumbers(l1, l2)

