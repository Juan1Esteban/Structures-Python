

class Array2D:
   def __init__(self, rows, cols):
      self.rows = rows
      self.cols = cols
      self.data = []
      for r in range(self.rows):
         tmp = []
         for c in range(self.cols):
            tmp.append(0)
         self.data.append(tmp)

   def get_num_rows(self):
      return self.rows
 
   def get_num_cols(self):
      return self.cols
 
   def clearing(self, value):
      for r in range(self.rows):
         for c in range(self.cols):
            self.data[r][c] = value
 
   def set_item(self, r, c, value):
      self.data[r][c] = value
 
   def get_item(self, r, c):
      return self.data[r][c]
 
   def to_string(self):
      res = ""
      for r in range(self.rows):
         for c in range(self.cols):
            res += str(self.data[r][c]) + " "
         res += "\n"
      return res


if __name__ == "__main__":

   matrix = Array2D(3, 3)
   matrix.clearing(0)
   matrix.set_item(0, 0, 1)
   print(matrix.to_string())



'''

La clase Array2D se utiliza para crear objetos que representan matrices bidimensionales. En la definición de la clase, se especifican los métodos que se pueden usar con estos objetos.

El método __init__ es el constructor de la clase, se invoca automáticamente cuando se crea un nuevo objeto de la clase Array2D. En este método, se especifican los atributos que se deben inicializar cuando se crea un objeto. 
En este caso, se especifican el número de filas y columnas de la matriz (rows y cols) y se crea una lista vacía data que almacenará los valores de la matriz. Después, se llena data con listas de ceros, para que cada elemento de data represente una fila de la matriz y cada elemento de cada fila represente una columna.

Los métodos get_num_rows y get_num_cols devuelven el número de filas y columnas de la matriz, respectivamente.

El método clearing permite establecer todos los elementos de la matriz a un valor específico. Se utiliza un bucle anidado para recorrer todas las filas y columnas de la matriz y establecer cada elemento en el valor especificado.

El método set_item permite establecer un elemento específico de la matriz en un valor específico. Se especifica la fila y la columna que se desea modificar, y el valor que se desea establecer.

El método get_item permite obtener el valor de un elemento específico de la matriz. Se especifica la fila y la columna del elemento que se desea obtener.

El método to_string permite convertir la matriz en una cadena de texto. Se utiliza un bucle anidado para recorrer todas las filas y columnas de la matriz y concatenar cada elemento en una cadena de texto. La cadena resultante se devuelve como resultado.

Por último, en el código que se muestra al final, se crea un objeto matrix de la clase Array2D con 3 filas y 3 columnas. Se llama al método clearing para establecer todos los elementos de la matriz en 0 y luego se llama al método set_item para establecer el elemento en la fila 0 y columna 0 en 1. 
Finalmente, se llama al método to_string para imprimir la matriz en formato de texto.

'''
