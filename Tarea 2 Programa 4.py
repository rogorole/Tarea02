#Programa 4
numero = float(input("Introduce el numero a redondear: "))
decimales = int(input("Decimales a redondear: "))

Cantidad = 10 ** decimales
redondeado = int(numero * Cantidad + 0.5) / Cantidad

print(f"El número redondeado a {decimales} decimales es: {redondeado}")
print("FIN DEL PROGRAMA")
