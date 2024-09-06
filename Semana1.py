# punto 1

nombre = input("Ingresa tu nombre: ")
apellido = input ("Ingresa tu apellido: ")

print("Bienvenido: ", nombre, apellido) 

# punto 2

precio = 100
descuento= precio *0.15

print ("El precio final es de: ", precio - descuento)

# punto 3

edad = int(input("Ingresa tu edad: "))

if edad>18:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")

# punto 4

numero = int(input("Integre un numero del 1 al 9: "))

if numero in [1,3,5,7,9]:
    print("El numero es impar")

elif numero in [2,4,6,8]:
    print ("El numero es par")
else:
    print("El numero ingresado es errado")


# punto 5

a1 = int(input ("Ingrese un primer numero: "))
a2 = int(input ("Ingrese un segundo: "))

print ("Resultado de la suma es: ", a1 + a2 )
print ("Resultado de la resta es: ", a1 - a2)
print ("Resultado de la multiplicación es: ", a1 * a2)
print ("Resultado de la división es: ", a1 / a2)

# punto 6

def calificacion():
    
    nota = int(input("Ingrese su calificación: "))

    if nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")

calificacion()

# punto 7

def encontrar_mayor():
    
    n1 = float(input("Ingrese el primer número: "))
    
    n2 = float(input("Ingrese el segundo número: "))
    
    if n1 > n2:
        print(f"El número mayor es: {n1}")
    elif n2 > n1:
        print(f"El número mayor es: {n2}")
    else:
        print("Ambos números son iguales.")

encontrar_mayor()

# punto 8

def saludo():
    
    nombre = input("Ingrese su nombre: ")
        
    print(f"¡Hola, {nombre}! Bienvenido al programa.")

saludo()

# punto 9

def tabla_multiplicar():
        
        numero = int(input("Ingrese un número: "))
        
        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    
tabla_multiplicar()

# punto 10

def calcular_promedio():

        n1 = float(input("Ingrese el primer número: "))
        
        n2 = float(input("Ingrese el segundo número: "))
        
        promedio = (n1 + n2) / 2
        
        print(f"El promedio de {n1} y {n2} es: {promedio}")
    
calcular_promedio()
