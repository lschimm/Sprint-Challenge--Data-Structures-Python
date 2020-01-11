from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # The `append` method adds elements to the buffer.
    def append(self, item):
        # let's see if it's full first as a base case
        # if it's full, we'll remove the head
        # then we'll need to reset the tail position
    
    # The `get` method returns all of the elements in the buffer in a list in their given order.
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
