# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #set a flag and mark each visited node as true and
        #if pointer to next of a node points to true then cycle exists

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow :
                return True
        return False
        