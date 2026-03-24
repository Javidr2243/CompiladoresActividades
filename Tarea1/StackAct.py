class Stack:
    def __init__(self):
        self.items = []  # lista para almacenar los elementos del stack

    def push(self, element):
        # agrega un elemento a la cima del stack
        self.items.append(element)

    def pop(self):
        # elimina y regresa el elemento de la cima (LIFO)
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # regresa el elemento de la cima sin eliminarlo
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # verifica si el stack está vacío
        return len(self.items) == 0

    def size(self):
        # regresa el número de elementos en el stack
        return len(self.items)


# --- Muestra el comportamiento LIFO ---
print("=== Demo del Stack ===")
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Se agregaron 10, 20, 30")
print("Pop:", s.pop())   # debe ser 30 (último en entrar, primero en salir)
print("Pop:", s.pop())   # debe ser 20
print("Peek:", s.peek())  # debe ser 10 (sigue en el stack)
print("Tamaño:", s.size())  # debe ser 1


# --- Casos de prueba ---
print("\n=== Pruebas ===")

# Prueba push: verifica que los elementos se agregan correctamente
s1 = Stack()
s1.push(1)
s1.push(2)
print("Prueba push - tamaño tras agregar 2 elementos:", s1.size())  # esperado: 2

# Prueba pop: verifica el orden LIFO — el último en entrar es el primero en salir
s2 = Stack()
s2.push("a")
s2.push("b")
print("Prueba pop - elemento eliminado:", s2.pop())  # esperado: b

# Prueba peek: verifica que podemos ver la cima sin eliminarla
s3 = Stack()
s3.push(99)
print("Prueba peek - elemento en la cima:", s3.peek())       # esperado: 99
print("Prueba peek - tamaño sin cambios:", s3.size())        # esperado: 1

# Prueba is_empty: verifica que se detecta correctamente si el stack está vacío
s4 = Stack()
print("Prueba is_empty - stack nuevo:", s4.is_empty())       # esperado: True
s4.push(5)
print("Prueba is_empty - después de push:", s4.is_empty())   # esperado: False

# Prueba size: verifica que el conteo se actualiza tras push y pop
s5 = Stack()
s5.push(1)
s5.push(2)
s5.push(3)
s5.pop()
print("Prueba size - tras 3 push y 1 pop:", s5.size())  # esperado: 2
