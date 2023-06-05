class Clientes:
    carrito = {}
    
    def __init__(self, nombre, apellido, email, telefono, pais, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.__telefono = telefono
        self.pais = pais
        self.__dni = dni
        
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, apellido: {self.apellido}, email: {self.email}, telefono: {self.__telefono}, pais: {self.pais}, dni: {self.__dni}'
    
    def comprar(self, producto, tienda):
        if producto in self.carrito:
              return print(f'El producto: {producto} ya se encuentra en el carrito')                  
        else:
            self.carrito.update({producto: tienda})
            return print(f'El producto: {producto} fue agregado')