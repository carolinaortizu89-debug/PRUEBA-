
#Sistema Rápido de Trazabilidad de Muestras de Laboratorio 

# 1 Estructura de Datos Principal: 

muestras_lab = []

# 2 Menú Principal (Bucle while): 

continuar = True
while continuar:
    print("SISTEMA DE CONTINGENCIA DE LABORATORIO")
    print("1 registrar una nueva muestra")
    print("2 buscar y gestionar muestra")
    print("3 salir")

    opcion = input("seleccione una opcion del uno al tres(1-3): ")

# 3 Opción 1: Registrar nueva muestra 
    
    if opcion == "1":
        print("registro de nueva muestra")
        codigo = input("ingrese el codigo de la muestra: ")
        nombre = input("ingrese el nombre del paaciente: ")
        temperatura = float(input("ingrese la temperatura de la muestra en grados celcius:"))
# logica de la cadena de frio
        if temperatura < 2 or  temperatura > 8:
            estado = "RECHAZADA"
            print("ALERTA MUESTRA FUERA DE LA CADENA DE FRIO, ESTADO : RECHAZADA")
        else:
            estado = "PENDIENTE"
            print(" Muestra deltro del rango correcto, estado: PENDIENTE")

        registro_completo = codigo + "-" + nombre + "-" + estado
        muestras_lab.append(registro_completo)
        print(" muestra resgistrada exitosamente")

# 4 opcion 2 Buscar y Gestionar Muestra 
    elif opcion == "2":
        print("buscar y gestiornar muestra")
        codigo_buscar = input("ingrese el codigo de la muestra a buscar: ")

        encontrado = False
        for i in range(len(muestras_lab)):
            if codigo_buscar in muestras_lab[i]:
                encontrado = True
                print("MUESTRA ENCONTRADA") 
                print("datos actuales: " + muestras_lab[i])
         #sub menu

                print("acciones disponibles")
                print("A actualizar estado")
                print("B desechar muestra")
                accion = input("seleccione una accion: ").lower()

                if accion == "A":
                    nuevo_estado = input("ingrese el nuevo estado: ").upper()
                    partes = muestras_lab[i].split(" - ")
                    muestras_lab[i] = partes[0] + " - " + nuevo_estado
                    print("estado actualizado correctamente")
                
                elif accion == "B":
                    muestras_eliminada = muestras_lab.pop(i)
                    print("muestra eliminada del sistema")
                else:
                    print("ACCION NO VALIDA")
                
                break

        if not encontrado:
             print("ERROR EL CODIGO DE MUESTRA INGRESADO NO EXISTE EN EL SISTEMA")

# 5 opcion 3 salida 

    elif opcion == "3":
        print("CERRANDO EL SISTEMA DE CONTINGENCIA")
        print ("HASTA PRONTO ASEGURESE DE REPORTAR LOS REGISTROS AL SISTEMA PRINCIPAL")
        continuar = False

    else:
          print("OPCION NO VALIDA POR FAVOR INTENTE CON UN NUMERO DE UNO A TRES")
                      
