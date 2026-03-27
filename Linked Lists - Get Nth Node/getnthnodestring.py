from preloaded import Node

def get_nth(node, index):
    if index < 0 or node is None:
        raise ValueError("Invalid index or empty list")
    
    current = node
    counter = 0
    
    while current is not None:
        if counter == index:
            return current
        
        current = current.next
        counter += 1
    
    raise IndexError("Index out of bounds")
