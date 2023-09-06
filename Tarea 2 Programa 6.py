#Programa 6
tornillo = int(input("Introduce un numero de tornillo del 0 al 23: "))

renglon = tornillo // 8
columna = tornillo % 8

x = 7.5 + 15 * columna
y = 7.5 + 15 * renglon

print(f"Las coordenadas x,y del tornillo {tornillo} son x={x} y y={y} mm.")
