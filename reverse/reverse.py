class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
        # TO BE COMPLETED
        # we'll be reversing like
        # from 1 > 2 > 3 > None
        # to 3 > 2 > 1 > None
        # so we need to set up the one, two, and three
        
        # use a while loop
        # break it if the first one isn't empty
        # first one will contain the head

        first = self.head
        second = None
        third = None
        

        # while first is not None:
              # if get_next == None:
              #       set_next

              # if the next value is None
              # set the next value to what is currently on top of the stack
              # 
              
              # first is currently NOT none; set to self.head
        while first is not None:
        #       # assign first.next_node to second
              second = first.next_node
        #       # first.next_node is swapped to third
              first.next_node = third
        #       # third is assigned to first
        #       # third is now in the first position
              third = first
        #       # and then first assigned to second
              first = second
        #       # then reassigning the head to third (it's at the beginning now)
              self.head = third
        #       # just to make extra suuure in case first never IS none (even though I assigned it myself....)
              if first is None:
                    break