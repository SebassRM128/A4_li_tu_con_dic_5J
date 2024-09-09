print("Ejemplos de tuplas")
canciones=("te amo","El Noa Noa","Amor")
print(canciones)
y = list(canciones)
y[1] = "La puerta negra"
x = tuple(y)
print(x)