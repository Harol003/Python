# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Polimorfismo")

class Ave:
    def volar(self):
        print("El ave está volando.")

class Murcielago(Ave):
    def volar(self):
        print("El murciélago está volando en la oscuridad.")

# Usar polimorfismo: el mismo nombre de método, pero diferente implementación
def hacer_volar(ave):
    ave.volar()

# Crear instancias de diferentes clases
ave = Ave()
murcielago = Murcielago()

# Polimorfismo: aunque ambos objetos usan el mismo método 'volar', tienen comportamientos diferentes
hacer_volar(ave)         # Salida: El ave está volando.
hacer_volar(murcielago)  # Salida: El murciélago está volando en la oscuridad.
