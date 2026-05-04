# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #attact next pointer to the prev but make sure to save curr.next in a temp
        #so that when we do curr.next = prev we can know what is the next val
        #move prev = curr
        # curr = temp.next
        prev = None
        if not head:
            return prev
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev