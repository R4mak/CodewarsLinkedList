def swap_pairs(head):
    dummy = Node()
    dummy.next = head
    current = dummy
    
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        
        current.next = second
        
        first.next = second.next
        
        second.next = first
        
        current = first
        
    return dummy.next
