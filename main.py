

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
   """ contador = 0

   while contador < 10:
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