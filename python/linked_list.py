class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head, length):
    self.head = head 
    self.length = length

  def add(self, data):
    # write your code to ADD an element to the Linked List
    pass

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pass

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    pass

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, data, next):
    self.data = data 
    self.next = next 
  pass
