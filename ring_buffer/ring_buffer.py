from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If NOT at capacity move forward
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        else: 
            # if you're in the middle of the list 
            if self.current.next is not None:
                self.current.next.value = item
                # Overwrite the value
                self.current = self.current.next      
                
            else: # we're at the end
                self.storage.head.value = item
                self.current = self.storage.head
                    

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        curr = self.storage.head
        # traverse the linked list and return the elements
        while curr is not None:
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------

# The disadvantage of arrays is typically the need to resize the array when it grows to large
# With a constrained array, we never have to worry about increasing the size of the array
# and look up access is much faster with known indexes

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity

    def get(self):
        return [x for x in self.storage if x is not None]                