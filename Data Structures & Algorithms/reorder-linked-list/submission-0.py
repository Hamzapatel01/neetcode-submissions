# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #split the list into half
        #reverse the second half
        #merger two of the halves one at a time

        node = slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = None
        slow.next = None

        #reverse the list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        #merge here:
        first = head
        second = prev
        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        
