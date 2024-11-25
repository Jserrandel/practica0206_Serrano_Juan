#Escribir un programa que cree un diccionario vacío
#y lo vaya llenado con información sobre una persona
#(por ejemplo nombre, edad, sexo, teléfono, correo
#electrónico, etc.) que se le pida al usuario.
#Cada vez que se añada un nuevo dato debe
#imprimirse el contenido del diccionario.

Vacio = {}
entrada = input("¿Cual es tu nombre? ")
Edad = input("¿Cual es tu edad? ")
Genero = input("¿Cual es tu genero? ")
Tfn = input("¿Cual es tu numero de telefono? ")
Correo = input("¿Cual es tu correo electronico? ")
Vacio['Nombre'] = entrada
Vacio['Edad'] = Edad
Vacio['Genero'] = Genero
Vacio['Numero de telefono'] = Tfn
Vacio['Correo electronico'] = Correo
print(Vacio)