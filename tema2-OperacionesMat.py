num1=20
num2=4

print("La suma: ", num1+num2)
print("La resta: ", num1-num2)
print("La multiplicacion: ", num1*num2)
print("La division: ", num1/num2)
print("La division exacta: ", num1//num2)
print("La potencia es: ", num1**num2)


#Concatenacion en python

texto1="Hola"
texto2="Mundo"
textoFinal=texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s " %(texto1,texto2))

saludo="El saludo es: {} {}".format(texto1,texto2)
print(saludo)

saludoFinal="Saludo 2: {x} {y}".format(x=texto1,y=texto2)
print(saludoFinal)

saludoFinal2=f"Saludo 3: {texto1} {texto2}"
print(saludoFinal2)
