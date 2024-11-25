#Escribir un programa que guarde en un diccionario
#los precios de los artículos de la tabla, pregunte
#al usuario por un artículo, un número de unidades
#y muestre por pantalla el precio de esa cantidad 
#de producto. Si el producto no está en el diccionario
#debe mostrar un mensaje informando de ello.
#Producto - Precio:
#Pan - 1.40€
#Huevos - 2.30€
#Cebolla - 0.85€
#Aceite - 4.35€
Productos = {"pan":1.40, "huevos":2.30, "cebolla":0.85, "aceite":4.35}
Producto = input("¿Que producto quieres? ")
Numero = float(input("¿Cuantos? "))
if Producto in Productos:
    print(Productos[Producto] * Numero)
else:
    print("No tenemos ese producto")