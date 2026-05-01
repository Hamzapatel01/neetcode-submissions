# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first go to the n
        # then do prev.next = curr.next
        # curr = curr.next

        curr = head
        count = 0

        while curr:
            count +=1
            curr = curr.next
            print(count)

        target = count - n #this is the position to remove the node in 0th indexed
        #go to that pointer and do next - next.next

        if target == 0 :
            return head.next
        curr = head
        for i in range(target - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
