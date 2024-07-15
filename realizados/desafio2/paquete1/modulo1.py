class Cliente: 
    def __init__( self, nombre, correo, edad, intereses):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.intereses = intereses

    def comprar(self, producto, lugar):
        print(f"{self.nombre} ha comprado {producto} en {lugar}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Edad: {self.edad}, Intereses: {', '.join(self.intereses)}"
