#cuenta regresiva: crea una funcion que aceptte un numero como enntrada. -devuelve una lista nueva que cuente de uno en uno, desde el numero 
# (como elemento 0 )
#hasta 0 (como ultimo elemento).

def countdown(num): #num = 5
    lista = [] #Creamos lista vacía, para ahí poner todos los números
    for i in range(num, -1, -1): #(num con el que comenzamos, parada, avance)
        lista.append(i)
        #lista += [i]

    return lista

def countdownWhile(num):
    lista = []
    while num > -1:
        lista.append(num)
        num -= 1
    return lista

#Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
def imprimir_y_devolver(lista): #lista = [1, 2]
   
    print(lista[0])
    return lista[1]

def primero_mas_longitud(lista):
    suma = lista[0] + len(lista)
    return suma

#Valores mayores que el segundo
#valores_mayores_que_el_segundo([5,2,3,2,1,4])
#lista = [5,2,3,2,1,4]
#nueva_lista = []
#numero = 5
#nueva_lista = [5]
#numero = 2
#numero = 3
#nueva_lista = [5, 3]
#numero = 2
#numero = 1
#numero = 4
#nueva_lista = [5, 3, 4]
#PRINT 3
#RETURN [5, 3, 4]
def valores_mayores_que_el_segundo(lista):
    nueva_lista = []
    if len(lista) < 2:
        return False
    else:
        for numero in lista:
            if numero > lista[1]:
                nueva_lista.append(numero)
        
        print(len(nueva_lista))
        return nueva_lista
        
        #length_and_value(4,7)
        #tamaño = 4
        #valor = 7
        #lista =[]
        #0 - 3
        #i = 0
        #lista = [7]
        #i = 1
        #lista = [7, 7]
        #i = 2
        #lista = [7, 7, 7]
        #i = 3
        #lista = [7, 7, 7, 7]
        #i = 4
        #-------------

        # RETURN 

        def length_and_value(tamaño, valor):
            lista = []
            for i in range (tamaño):
                lista.append(valor)

            return lista    


        

