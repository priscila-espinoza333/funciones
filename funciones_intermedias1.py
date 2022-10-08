#Pregunta 1
#Ejercicio 1
x = [ [5,2,3], [10,8,9] ] 

#Ejercicio 2
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

#Ejercicio 3
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

#Ejercicio 4
z = [ {'x': 10, 'y': 20} ]

        # *****   DESARROLLO *****

#Desarrollo ejercicio 1
#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print(x)

#Desarrollo ejercicio 2
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

#Desarrollo ejercicio 3
#En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

#Desarrollo ejercicio 4
#Cambia el valor 20 en z a 30.

z[0]['y'] = 30
print(z)

#----------------------------------------

#Pregunta 2
#Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios
# de la lista e imprima cada llave y el valor asociado.

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    
def iterateDictionary(some_list):
    new =''
    for dictionary in some_list:
        new += f"first_name - {dictionary['first_name']}, last_name - {dictionary['last_name']}\n"
    print(new)

iterateDictionary(estudiantes)

#----------------------------------------

#Pregunta 3
#Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario.
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name, some_list):
    new=''
    for dictionary in some_list:
        new += f"{dictionary[key_name]}\n"
    print(new) 
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes) 

# -----------------------------------------

#Prefunta 4
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave
#junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. 

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dictionary):
    for n in (dictionary):
        print(len(dictionary[n]),n) 
        for d  in dictionary[n]:
            print (d)
printInfo(dojo)










