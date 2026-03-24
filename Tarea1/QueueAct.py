from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()  # deque de la librería collections para manejo eficiente

    def enqueue(self, element):
        # agrega un elemento al final de la cola
        self.queue.append(element)

    def dequeue(self):
        # elimina y regresa el elemento del frente (FIFO)
        return self.queue.popleft() if not self.is_empty() else None

    def front(self):
        # regresa el elemento del frente sin eliminarlo
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        # verifica si la cola está vacía
        return len(self.queue) == 0

    def size(self):
        # regresa el número de elementos en la cola
        return len(self.queue)


# --- Muestra del comportamiento FIFO ---
print("=== Demo de la Cola ===")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Se agregaron 10, 20, 30")
# debe ser 10 (primero en entrar, primero en salir)
print("Dequeue:", q.dequeue())
print("Dequeue:", q.dequeue())  # debe ser 20
print("Front:", q.front())      # debe ser 30 (sigue en la cola)
print("Tamaño:", q.size())      # debe ser 1


# --- Casos de prueba ---
print("\n=== Pruebas ===")

# Prueba enqueue: verifica que los elementos se agregan correctamente
q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
print("Prueba enqueue - tamaño tras agregar 2 elementos:", q1.size())  # esperado: 2

# Prueba dequeue: verifica el orden FIFO — el primero en entrar es el primero en salir
q2 = Queue()
q2.enqueue("a")
q2.enqueue("b")
print("Prueba dequeue - elemento eliminado:", q2.dequeue())  # esperado: a

# Prueba front: verifica que podemos ver el frente sin eliminarlo
q3 = Queue()
q3.enqueue(99)
print("Prueba front - elemento al frente:", q3.front())     # esperado: 99
print("Prueba front - tamaño sin cambios:", q3.size())      # esperado: 1

# Prueba is_empty: verifica que se detecta correctamente si la cola está vacía
q4 = Queue()
print("Prueba is_empty - cola nueva:", q4.is_empty())       # esperado: True
q4.enqueue(5)
print("Prueba is_empty - después de enqueue:",
      q4.is_empty())  # esperado: False

# Prueba size: verifica que el conteo se actualiza tras enqueue y dequeue
q5 = Queue()
q5.enqueue(1)
q5.enqueue(2)
q5.enqueue(3)
q5.dequeue()
print("Prueba size - tras 3 enqueue y 1 dequeue:", q5.size())  # esperado: 2
