#Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
#Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
#Preguntar por el NIF del alumno/a y mostrar sus datos.
#Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
#Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
#Terminar el programa.
alumnado = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del alumno/a: ')
        nombre = input('Introduce el nombre del alumno/a: ')
        apellidos = input('Introduce los apellidos del alumno/a: ')
        telefono = input('Introduce el teléfono del alumno/a: ')
        email = input('Introduce el correo electrónico del alumno/a: ')
        aprobado = input('¿Ha aprobado el módulo (S/N)? ')
        alumno = {'nombre': nombre, 'apellidos': apellidos, 'teléfono': telefono, 'email': email, 'aprobado': aprobado == 'S'}
        alumnado[nif] = alumno
    if opcion == '2':
        nif = input('Introduce NIF del alumno/a: ')
        if nif in alumnado:
            del alumnado[nif]
        else:
            print('No existe el alumno/a con el NIF', nif)
    if opcion == '3':
        nif = input('Introduce NIF del alumno/a: ')
        if nif in alumnado:
            print('NIF:', nif)
            for clave, valor in alumnado[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el alumno/a con el NIF', nif)
    if opcion == '4':
        print('Lista de todo el alumnado')
        for clave, valor in alumnado.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista del alumnado aprobado')
        for clave, valor in alumnado.items():
            if valor['aprobado']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir alumno/a\n(2) Eliminar alumno/a\n(3) Mostrar alumno/a\n(4) Listar todo el alumnado\n(5) Listar alumnado aprobado\n(6) Terminar\nElige una opción: ')
