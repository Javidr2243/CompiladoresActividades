
class Dictionary:
    def __init__(self):
        # dict de Python para guardar los pares clave-valor
        self.data = {}

    def put(self, key, value):
        # inserta o actualiza un valor con su clave
        self.data[key] = value

    def get(self, key):
        # regresa el valor de la clave, o None si no existe
        return self.data.get(key, None)

    def remove(self, key):
        # elimina la clave si existe
        if key in self.data:
            del self.data[key]

    def contains_key(self, key):
        # revisa si la clave está en el diccionario
        return key in self.data

    def size(self):
        # regresa cuántos pares hay
        return len(self.data)


# Muestra de las operaciones básicas
print("=== Demo Diccionario ===")
d = Dictionary()
d.put("nombre", "Juan")
d.put("edad", 20)
d.put("carrera", "Sistemas")
print("nombre:", d.get("nombre"))
print("edad:", d.get("edad"))

d.put("edad", 21)  # actualizar valor
print("edad actualizada:", d.get("edad"))

d.remove("carrera")
print("después de borrar carrera, tamaño:", d.size())  # 2


# pruebas
print("\n=== Pruebas ===")

# put: Inserta dos pares y revisa que el tamaño sea 2
d1 = Dictionary()
d1.put("a", 1)
d1.put("b", 2)
print("put - size:", d1.size())  # esperado: 2

# get: revisa que regrese el valor correcto para una clave existente
d2 = Dictionary()
d2.put("x", 99)
print("get - valor:", d2.get("x"))  # esperado: 99

# get caso borde: clave que no existe debe regresar None
print("get clave inexistente:", d2.get("z"))  # esperado: None

# remove: borra una clave y revisa que ya no esté
d3 = Dictionary()
d3.put("k", 5)
d3.remove("k")
print("remove - contains 'k':", d3.contains_key("k"))  # esperado: False

# remove caso borde: borrar clave que no existe
d3.remove("k")
print("remove inexistente: ok")

# contains_key: revisa si una clave existe o no
d4 = Dictionary()
d4.put("py", "Python")
print("contains 'py':", d4.contains_key("py"))    # esperado: True
print("contains 'js':", d4.contains_key("js"))    # esperado: False

# size: 3 inserts y 1 borrado deben dejar tamaño 2
d5 = Dictionary()
d5.put(1, "uno")
d5.put(2, "dos")
d5.put(3, "tres")
d5.remove(2)
print("size:", d5.size())  # esperado: 2
