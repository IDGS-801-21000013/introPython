print("Suma de numeros")
num1=int(input("Dame n1:"))
num2=int(input("Dame n2:"))

print(f"La suma de los numeros {num1} y {num2} es: {num1+num2}")

if num1>num2:
    print(f"El numero mayor es: {num1}")
else: 
    print(f"El numero mayor es: {num2}")

print("---------------------Pedir una edad----------------------")
edad=int(input("Ingresa tu edad:"))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")