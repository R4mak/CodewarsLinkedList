def stringify(node):
    result = []
    current = node
    
    while current is not None:
        result.append(str(current.data))
        current = current.next
    
    result.append("None")
    
    return " -> ".join(result)
