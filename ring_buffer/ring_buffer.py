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


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
