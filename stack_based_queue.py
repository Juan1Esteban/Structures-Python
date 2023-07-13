

class TwoWayStackP:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()
    

"""
x = Queue()
x.enqueue(5)
x.enqueue(6)
x.enqueue(7)
print(x.inbound_stack)
x.dequeue()
print(x.inbound_stack)
print(x.outbound_stack)
x.dequeue()
print(x.outbound_stack)
"""


class TwoWayStackC:
   def __init__(self):
      self.stack1 = []
      self.stack2 = []

   def enqueue(self, item):
      # Agregar el elemento al stack1
      self.stack1.append(item)

   def dequeue(self):
      # Si stack2 está vacío, transferir los elementos de stack1 a stack2 en orden inverso
      if not self.stack2:
         while self.stack1:
            self.stack2.append(self.stack1.pop())
      # Devolver el primer elemento de stack2
      return self.stack2.pop()

'''
# Crear una cola vacía
q = Queue()

# Agregar elementos a la cola
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Eliminar elementos de la cola
print(q.dequeue())  # Devuelve 1
print(q.dequeue())  # Devuelve 2
print(q.dequeue())  # Devuelve 3
'''
