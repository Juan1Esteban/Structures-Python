from node import Node

class CircularLinkedList:
   def __init__(self):
      self.head = None
    
   def append(self, value):
      new_node = Node(value)
      if self.head is None:
         self.head = new_node
         new_node.next = self.head
      else:
         current = self.head
         while current.next != self.head:
            current = current.next
         current.next = new_node
         new_node.next = self.head
    
   def print_list(self):
      current = self.head
      while current:
         print(current.value)
         current = current.next
         if current == self.head:
            break
