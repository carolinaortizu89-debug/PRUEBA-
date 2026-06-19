#sistema rapido de trazabilidad de muestras de laboratorio 

muestra_lab =[]

while True:
    print("\n menu principal")
    print("1. registrar nueva muestra")
    print("2.buscar y gestionar muestra")
    print("3. salir")

opcion = input("escoge una opcion:")

# registrar 
if opcion == "1":
    codigo = input("codigo de la muestra (ej: M001): ").strip()
    nombre = input("nombre del paciente:" ).strip()
    temp = float(input("temperatura (°c): "))

# cadena de frio
if temp < 2 or temp > 8:
    estado = "rechazada"
else:
    estado = "pendiente"

registro = f"{codigo} - {nombre} - {estado}"
muestra_lab.append(registro)

print(" muestra registrada:", registro)

# buscar y gestionar

elif opcion == "2":
    buscar = input("ingresa el codigo de la muestra ").strip()
    encontrada = False
    for i, muestra in enumerate(muestras_lab):
        if muestra.startswhit(buscar):
        encontrada = True
        print("\nMuestra encontrada", muestra)


# salir
elif opcion == "3":
    print(" gracias por usar el sistema ")
    break
else:
print("opcion invalida. intenta de nuevo.")


