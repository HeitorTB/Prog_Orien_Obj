#Exercício 1
num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
PROD = num1*num2
print("PROD = ",PROD)

#Exercício 2
Nota1= float(input("digite a primeira nota: "))
Nota2= float(input("digite a segunda nota: "))
Media = (Nota1*3.5 + Nota2*7.5) /11
print("MEDIA = ", format(Media, ".5f"))

#Exercício 3
pi = 3.14159
raio = int(input("Digite o raio da esfera: "))
volume = (4/3) * pi * raio**3
print(format(volume, ".3f"))

#Exercício 4
C, N = map(int, input("Digite os metros corridos e o tamanho da pista: ").split())
print(C%N)

#Exercício 5
import math
x1, y1 = map(int, input("Digite o valor de x1 e y1: ").split())
x2, y2 = map(int, input("Digite o valor de x2 e y2: ").split())
calc= math.sqrt((x2-x1)**2 + (y2 - y1)**2)
print("{:.4f}".format(calc))

#Exercício 6
T1, T2, T3, T4 = map(int, input("Digite 4 números para as respectivas réguas: ").split())
total_tomadas = (T1 - 1) + (T2 - 1) + (T3 - 1) + T4
print(total_tomadas)



