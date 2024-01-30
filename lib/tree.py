class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_traverse = [self.root]
    while len(nodes_to_traverse) > 0:
      node = nodes_to_traverse.pop(0)
      if node['id'] == id:
        return node 
      else:
        nodes_to_traverse = node["children"] + nodes_to_traverse
    return None
