#Exercício 1
nome = input("Digite seu nome completo: ")
pnome=""
for letra in nome:
    if letra == " ":
        break
    else:
        pnome+=letra
print("Bem vindo(a) ao Python", pnome)

#Exercício 2
nota1 = int(input("Digite a nota do primeiro bimestre da diciplina: "))
nota2 = int(input("Digite a nota do segundo bimestre da diciplina: "))
media = (nota1*2 + nota2*3)//5
print("A média é igual a ",media)

#Exercício 3
import math
Altura = float(input("Digite a base do retângulo: "))
Base = float(input("Digite a altura do retângulo: "))
Area= Altura*Base
Perímetro = (Altura*2)+(Base*2)
Diagonal = math.sqrt(Altura**2 + Base**2)
print("Área: ",format(Area, ".2f"), "- Perímetro: ", format(Perímetro, ".2f"), "- Diagonal", format(Diagonal, ".2f"))

#Exercício 4
frase = input("Digite uma frase:\n")
ultima_palavra = frase[frase.rfind(" ") + 1:]
print(ultima_palavra)





