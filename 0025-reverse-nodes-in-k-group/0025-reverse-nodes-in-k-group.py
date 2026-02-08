class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        
        while curr:
            n += 1
            curr = curr.next
        
        swaps = n // k

        dummy = ListNode(0)
        dummy.next = head
        
        prev_g = dummy
        curr = head

        for _ in range(swaps):
            group_start = curr  
            prev = None

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            prev_g.next = prev
            group_start.next = curr
            
            prev_g = group_start

        return dummy.next
