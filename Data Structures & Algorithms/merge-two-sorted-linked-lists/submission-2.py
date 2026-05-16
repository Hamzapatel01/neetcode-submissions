# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #make a new linkedlist instead of maipulating pointers
        #if l1.value < l2.value insert l1 first and do l1.next as l2.val
        #and opposite if else is true

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            # print(dummy.val)
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next           