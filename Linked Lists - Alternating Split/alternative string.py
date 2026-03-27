class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes to split.")

    first_head = head
    second_head = head.next
    
    curr1 = first_head
    curr2 = second_head
    
    temp = second_head.next
    
    while temp:
        curr1.next = temp
        curr1 = curr1.next
        temp = temp.next
        
        if temp:
            curr2.next = temp
            curr2 = curr2.next
            temp = temp.next
        else:
            curr2.next = None
            
    curr1.next = None
    if temp is None:
        curr2.next = None

    return Context(first_head, second_head)
