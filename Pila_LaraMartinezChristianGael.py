#Lara Martinez Christian Gael 19/09/2023 ->Implementacion de Pila<-
class Pila:

    def __init__(self, size):
        self.lista = []
        self.tope = 0
        self.size = size

    # Verificamos si hay datos en la pila
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False

    # Agregar datos a la pila
    def push(self, dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            self.size += 5
            self.lista += [dato]
            self.tope += 1

    # Eliminar datos en la pila
    def pop(self):
        if self.empty():
            print("La pila está vacía")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    # Mostrar pila
    def show(self):
        i = self.tope - 1
        while i > -1:
            print(f"[{i}] => {self.lista[i]}")
            i -= 1

    # Mostrando la cima de la pila
    def top(self):
        return self.lista[-1]


if __name__ == "__main__":
    opcion = 0
    pila = Pila(5)
    while opcion != 6:
        print("---PILAS---")
        print("1.- Agregar Dato")
        print("2.- Eliminar Dato")
        print("3.- ¿Está vacia la pila?")
        print("4.- Mostrar la Pila")
        print("5.- Mostrar la cima de la pila")
        print("6.- Salir")
        opcion = int(input("Ingrese su opción "))

        if opcion == 1:
            dato = int(input("Ingresa un número "))
            pila.push(dato)
        elif opcion == 2:
            pila.pop()
        elif opcion == 3:
            print("SI" if pila.empty() else "NO")
        elif opcion == 4:
            pila.show()
        elif opcion == 5:
            print(pila.top())
        elif opcion == 6:
            print("\n--- Sesión culminada ---")
        else:
            print("Ingresaste una opción errónea, vuelve a intentarlo.")