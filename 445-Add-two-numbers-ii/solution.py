from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = val2 = ""
        while l1 or l2:
            if l1:
                val1 += str(l1.val)
                l1 = l1.next
            if l2:
                val2 += str(l2.val)
                l2 = l2.next
        val1 = int(val1)
        val2 = int(val2)
        newVal = val1 + val2
        newVal = str(newVal)
        h1 = ListNode(newVal[0])
        ptr = h1
        for i in range(1, len(newVal)):
            ptr.next = ListNode(newVal[i])
            ptr = ptr.next
        return h1


# Helper function to create a linked list from a list of values
def createLinkedList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


# Test the solution
list1 = [7, 2, 4, 3]
list2 = [5, 6, 4]

l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print("Resultant Linked List:")
printLinkedList(result)
