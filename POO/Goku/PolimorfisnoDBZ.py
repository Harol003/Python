# Mostrar el nombre, asignatura y tema
print("Politecnico Internacional")
print("Asignatura: Algoritmos 2")
print("Tema: Polimorfismo")

class Guerreros:
    def atacar(self):
        pass

class Goku(Guerreros):
    def atacar(self):
        return "Kamehameha"

class Vegeta(Guerreros):
    def atacar(self):
        return "Final Flash"

# Función polimórfica
def realizar_ataque(guerrero):
    print(f"{guerrero.atacar()}")

# Crear instancias de Goku y Vegeta
goku = Goku()
vegeta = Vegeta()

# Polimorfismo: Ambos guerreros tienen el método 'atacar()', pero con comportamientos diferentes
realizar_ataque(goku)   # Salida: Kamehameha
realizar_ataque(vegeta) # Salida: Final Flash
