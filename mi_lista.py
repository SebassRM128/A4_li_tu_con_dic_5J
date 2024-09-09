print("Ejemplo de listas")
arcoiris=["verde","azul","morado"]
print(arcoiris)
longitud=len(arcoiris)
print(longitud)
print("Elementos que contiene la lista arcoiris ", longitud)
print(f"Elementos que contiene la lista arcoiris v2 {longitud}")
print("accediendo a un elemento de la lista")
print(arcoiris[1])
print(f"elemento en la posicion 0 es {arcoiris[0]}")
print(f"El primer color del arcoiris es:",arcoiris[0])
print("agregar un elemento a la lista")
print(arcoiris)
arcoiris.append( "naranja")
print(arcoiris)
print("Listar los elementos de la lista ciclo for")
for rojas in arcoiris:
    print(rojas)
    