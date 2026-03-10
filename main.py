

print("hola mundo!")

#variables:

nombre = "Pablo"
edad = 27
altura = 1.67
es_diestro = False
ciudad = "Rancagua"
genero = ["hombre", "mujer", "therian", True, 1]

#TIPOS DE DATOS

str #esto es un texto
int #esto es un entero
float #esto es un flotante
bool #esto es verdadero o falso

#INPUT
#input()

texto = input() 
print(texto)

#numero =int(input( "escribe un numero : "))
#resultado = numero + 1
#print (resultado)
#

#INPUT SOLO AGARRA STR(TXT)
""" precio = input("escribe un precio :") #pedir por consola un tipo de dato tipo str
precio = int(precio) #convertir a entero el str con int(precio)
resultado = precio + 10 # el precio sumado + 10 ya que ahora es un numero entero
print(resultado) #imprimeme el precio en pantalla  """

## CONDICIONALES es una pregunta que le hacemos a una variable

#if condicion:
#   codigo:

""" == igual
!= diferente
> mayor
< menor
>= mayor o igual
<= menor o igual
 """

""" edad = 20

if edad >= 18:
   print("puede entrar a la disco") 
elif edad >= 50:
   print("demasiado antiguo!")
else:
   print("no puede entrar a la disco")    """

#BLUCES

#WHILE  necesita una condicion/ mientras sea true, se mantendrá en un bucle hasta que de un false
#while condicion:
 #    codigo
 #wile significa mientras pase algo 
    

""" while contador < 10:
 print(contador) contador = 0
 contador += 1
    
while True:
texto = input("escribe para salir del bulce")

if texto == "salir":
break """
   
   
 #FOR  necesita una lista/mientras tenga datos que iterar se mantendrá en bucle

 #for elemento in lista
#    codigo

lista = [1,2,3,4,5,6,7,8,9]

for i in lista: 
    print(i)

##LISTAS
lista = [1,2,3,4,5,6] ##CORCHETES SON IMPORTANTES
      
diccionario = {"key":"value"} #LLAVE VALOR

##SETS

sets = {1,2,3,4,5,6}

#TUPLAS 
tuplas = (1,2,3,4,5) #UNA VEZ QUE SE CREA LA TUPLAS NO SE PUEDE MODIFICAR """

#LISTAS
##INDEX
frutas = ["manzana","uva","kiwi","sandia", [1,2,3,4,[5,6,7]]]
    #INDEX    0       1      2       3          4          = POSICIÓN
    #        -5      -4     -3      -2         -1
frutas = [3] = "pera"
frutas = [0] = "melon"
frutas = [4] = [] #LISTA VACÍA

print(frutas[2]) 
print(frutas[1])  
print(frutas[0])
print(frutas[4][4][0])

print (frutas [3])
print (frutas [0])


print(frutas[-1]) #LLAMA AL ULTIMO ELEMENTO DE LA LISTA

#print(dir(frutas))

#APPEND
#FUNCIONES VAN CON ()
frutas.append("naranja") #AGREGA UN ITEM AL FINAL DE LA LISTA
print (frutas)

#REMOVE
frutas.remove("kiwi")

personas = ["crisitan","esteban"]

for i in personas:
    print(i)

alumnos = [] #lista vacía

while True:
    nombre = input ("ingresa un nombre de un alumno :")

    if nombre == "salir": 
        break
    alumnos.append(nombre)
print(alumnos) #DENTRO DE LA ITERACIÓN SE MUESTRA EN CONSOLA INMEDIATAMENTE JUNTO CON LO QUE SE VAYA AGREGANDO

print(alumnos) #FUERA DEL ITERACIÓN SE VA EJECUTANDO Y DENTRO DE LA CONSOLA SE VAN AGREGANDO LOS DATOS, CUANDO SE ROMPA LA ITERACIÓN APARECERAN LOS DATOS INGRESADOS

while True:
    print(---------menú")
    print("opcion 1 agregar")
    print("opcion 2 borrar")
    print("opcion 3 actualizar")
    print("opcion 4 salir")
opcion = input("ingresa al alumno")

if opcion == "1":
   nombre = input("ingresa el nombre alumno")
   alumnos.append(nombre)
   print(alumnos)
elif opcion == "2":
     nombre = input("ingresa el nombre alumno")
     alumnos.remove(nombre)
     print(alumnos)
elif opcion == 3:
     print("buscar alumno")
else:
    break 

alumnos[2] = nombre



##DICCIONARIOS



