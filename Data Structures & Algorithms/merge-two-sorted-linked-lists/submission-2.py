# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr1 = list1
        curr2 = list2
        currNode = dummy
        head = None
        if curr1 == None:
            return curr2
        if curr2 == None:
            return curr1

        while True:
            if curr1 == None or curr2 == None:
                break
            if curr2.val < curr1.val:
                currNode.next = curr2
                curr2 = curr2.next
            else:
                currNode.next = curr1
                curr1 = curr1.next
            currNode = currNode.next
        if curr1 == None:
            # curr2 may still have some nodes remaining
            # Set currNode to the same as the remaining curr2 list
            currNode.next = curr2
        if curr2 == None:
            currNode.next = curr1
        return dummy.next
            
        