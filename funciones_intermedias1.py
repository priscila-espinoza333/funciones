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

#pregunta 1
#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

x[1][0] = 15
print(x)

#pregunta 2
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes = [0]['last_name'] = 'Bryant'
print(estudiantes)

#pregunta 3
#En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes ['futbol'] [0] = 'Andres'
print(directorio_deportes)

#pregunta 4
#Cambia el valor 20 en z a 30.

z[0]['y'] = 30
print(z)



