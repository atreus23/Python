from Modulo.clientes import Clientes
       
cliente1 = Clientes("Luis", "Tecchio", "tecchio2013@gmail.com", 3515080450, "Argentina", 39421949)

print(cliente1)
print(cliente1.carrito)
cliente1.comprar("tablet", "apple")
cliente1.comprar("tablet", "apple")
cliente1.comprar("tablet1", "apple")
cliente1.comprar("tablet1", "apple")
print(cliente1.carrito)