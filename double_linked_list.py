from node import Node
        
class DoublyLinkedList:
   def __init__(self):
      self.head = None
        
   def append(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = new_node
      else:
         current = self.head
         while current.next:
            current = current.next
         current.next = new_node
         new_node.prev = current
            
   def prepend(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = new_node
      else:
         self.head.prev = new_node
         new_node.next = self.head
         self.head = new_node
            
   def print_list(self):
      current = self.head
      while current:
         print(current.data)
         current = current.next
