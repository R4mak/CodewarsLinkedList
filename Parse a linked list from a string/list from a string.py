from preloaded import Node

def linked_list_from_string(list_repr):
    parts = list_repr.split(" -> ")
    
    data_parts = parts[:-1]
    
    current_node = None
    
    for value in reversed(data_parts):
        current_node = Node(int(value), current_node)
    
    return current_node
