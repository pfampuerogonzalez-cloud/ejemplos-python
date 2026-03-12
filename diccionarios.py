""" ##DICCIONARIOS
#una estructura de datos
#estructura para guardar datos un poco más complejos.

#que guarda datos en formato clave, valor
# clave : valor
# "nombre" : "Pablo"


persona = {
    "nombre" : "carlos",
    "edad" : 28,
    "dirección" : "calle falsa 123", 
    "ciudad" : "Rancagua"
}


#modiciar valores

persona ["edad"] = 35
persona ["nombre"] = "carla"

#print(persona)

#agregar  un dato nuevo

persona["pais"] = "chile"
persona ["altura"]= 190
         
print persona

#iterar keys

for k in persona: 
    print(k)

#iterar values
for v in persona:
    print(v)

#iterar todo
for k, v in persona.items():
    print (k,v) 








    #LISTA DE DICCIONARIO DE ALUMNOS

    alumnos = [] """



while True:
       
       print("-------menu--------")
       print("1. agregar alumno")
       print("2. ver alumnos")
       print("3. salir")

       opcion = input("elige una opcion")

       if opcion == "1":
           nombre = input("nombre de alumno")
           edad = input("edad del alumno")

           alumno = {
               "nombre":nombre,
               "edad": edad
           }
           alumnos.append(alumno)

           print("alumno agregado!!!!")
           break
           
     elif opcion == "2":
           
         print("------lista de alumnos------")
           
           for alunmo in alumnos:
                print(alumno["nombre"], "--",alumno["edad"])
                
    elif opcion =="3":
        print("programa cerrado")
        break
    else:
         print("opcion no correcta solo se acepta 1,2 y 3 programa cerrado")
            break