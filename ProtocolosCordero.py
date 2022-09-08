from fileinput import close
import os

print("______________________________________________________________")
print("Bienvenido al creador de protocolos, Usuario...")
print("Escoja una de las siguientes opciones: ")
def menu():
    print('''
1.-Crear Protócolo
2.-Agregar paso a Protocolo
3.-Borrar Protocolo
4.-Ver Protocolo
5.-Salir del generador de Protocolos
________________________________________________________________
''')
a=0
menu()
print("Introduzca S o N si desea o no activar el generador de protocolos S-N: [ ] ")
opc = input("Introduzca la opción:  ")
if (opc == "N" or opc == "s" or opc == "S" or opc == "n"):

    print("Escriba el número de la opción a elegir")
    while (opc == "s" or opc == "S"):
        opcion=int(input("¿Qué número de opción escoge?  "))
        
        if opcion == 1:
            print("________________________________________________________________")
            name=input("Escribe el nombre del Protocolo: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            print("¿Desea escribir una instrucción? S-N")
            esc = input("--- ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print("________________________________________________________________")
                instruccion=input("Escribe la "+str(a)+"° instrucción: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                print("¿Quieres agregar una subinstrucción? S-N")
                sub=input("---  ")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escribe subinstrucción: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                print("¿Escribir otra instrucción? S-N")
                esc=input("---  ")
            print("Protocolo terminado")
            protocolo.close()
            
        elif  opcion == 2:
            print("________________________________________________________________")
            
            print("Escriba el nombre del protocolo a modificar: ")
            name = input("Protocolo:  ")
            print(" ")
            print(" ")
            print('''-----ATENCION-----''')
            print("Los pasos que se agregen al protocolo se mostrarán con un asterisco (*) para aclarar que se escribió como un añadido")
            print(" ")
            print(" ")
            protocolo = open(name + ".txt",'a')
            
            print("¿Agregar modificación? S-N ")
            esc= input("Introduzca la opción:  ")
            while (esc == "s" or esc=="S"):

                print("________________________________________________________________")
                print("Escriba la nueva instrucción: ")
                instruccion=input("Instrucción:  ")
                protocolo.write("*"+ instruccion + '''\n''')
                
                print("¿Quieres agregar una subinstrucción? S-N")
                sub=input("Introduzca la opción:  ")
                
                if (sub == "s" or sub=="S"):
                    
                    print("Escriba la subinstrucción: ")
                    subinstruccion=input("Subinstrucción:  ")
                    protocolo.write("    *"+subinstruccion+'''\n''')
                    
                print("¿Agregar otra instrucción? S-N ")
                esc=input("Introduzca la opción:  ")
            print("El protocolo "+name+ " ya fue modificado")
            protocolo.close()
            
            
        elif  opcion == 3:
            print("________________________________________________________________")
            print("Escribe el nombre del Protocolo que quieras borrar: ")
            name=input("Protocolo: ")
            os.remove(name + ".txt")
            print("El Protocolo " +name+ " fue borrado")
            
        elif  opcion == 4:
            print("________________________________________________________________")
            print("Escribe el nombre del Protocolo que quieras ver: ")
            name=input("Protocolo:  ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()

        elif opcion == 5:
            print("________________________________________________________________")
            print("Hasta luego")
            break
                   
        print("¿Desea elegir otra opción del menú? S-N")
        opc=input("Introduzca la opción:  ")
        if (opc=="s" or opc=="S"):
            continue
else:
    print("Hasta luego")
    