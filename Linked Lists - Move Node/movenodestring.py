class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError("Source list cannot be empty")
    
    node_to_move = source
    
    new_source = source.next
    
    node_to_move.next = dest
    new_dest = node_to_move
    
    return Context(new_source, new_dest)
