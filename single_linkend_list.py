from node import Node

class LinkedList:
   def __init__(self):
      self.head = None

   # Agregar un nuevo nodo al final de la lista
   def add(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = new_node
      else:
         current_node = self.head
         while current_node.next != None:
            current_node = current_node.next
         current_node.next = new_node

   # Eliminar el primer nodo con el valor especificado
   def remove(self, data):
      if self.head is None:
         return
      if self.head.data == data:
         self.head = self.head.next
         return
      current_node = self.head
      while current_node.next != None:
         if current_node.next.data == data:
            current_node.next = current_node.next.next
            return
         current_node = current_node.next

   # Imprimir los valores de todos los nodos en la lista
   def print_list(self):
      if self.head is None:
         print("La lista está vacía")
      else:
         current_node = self.head
         while current_node != None:
            print(current_node.data)
            current_node = current_node.next

if __name__ == "__main__":
   my_list = LinkedList()
   my_list.add(5)
   my_list.add(10)
   my_list.add(15)
   my_list.print_list()  

   
   my_list.remove(10)
   my_list.print_list() 
   


'''

from node import Node

class LinkedList:
   def __init__(self):
       self.head = None
       self.size = 0

   def add_to_head(self, value):
      new_node = Node(value)
      new_node.next = self.head
      self.head = new_node
      self.size += 1

   def remove_head(self):
      if self.head == None:
         removed_node = self.head
         self.head = self.head.next
         removed_node.next = None
         return removed_node.value
      else:
         return None

   def search(self, value):
      current = self.head
      while current == None:
         if current.value == value:
            return current
         current = current.next
      return None

   def __len__(self):
      return self.size               

'''

