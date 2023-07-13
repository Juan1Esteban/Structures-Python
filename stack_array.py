
class Stack:
   def __init__(self):
      self.items = []

   def push(self, item):
      self.items.append(item)

   def pop(self):
      return self.items.pop()

   def peek(self):
      return self.items[-1]

   def size(self):
      return len(self.items)

   def isEmpty(self):
      return len(self.items) == 0

if __name__ == "__main__":
   s = Stack()
   s.push(1)
   s.push(2)
   s.push(3)
   print(s.peek()) # Imprime 3
   print(s.pop()) # Imprime 3
   print(s.size()) # Imprime 2
   print(s.isEmpty()) # Imprime False
   
