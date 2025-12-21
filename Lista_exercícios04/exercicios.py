#Exercício 1
import math
A, B, C = map(float, input("Digite os valores de A, B, C: ").split())
if A == 0 or B**2 - 4*A*C < 0:
    print("Impossivel calcular")
else:
    delta = math.sqrt(B**2 - 4*A*C)
    R1 = (-B + delta) / (2 * A)
    R2 = (-B - delta) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

#Exercício 2
A, B = map(int,input("Digite o número 1 e o número 2: ").split())
if A % B == 0:
    print("São Multiplos")
else:
    print("Não são Multiplos")

#Exercício 3
V1= input("Primeira informação: ")
V2= input("Segunda informação: ")
V3= input("Terceira informação: ")
list=[V1, V2, V3]
if "vertebrado" in list and "ave" in list and "carnívoro" in list:
    print("águia")
elif "vertebrado" in list and "ave" in list and "onívoro" in list:
    print("pomba")
elif "vertebrado" in list and "mamífero" in list and "onívoro" in list:
    print("homem")
elif "vertebrado" in list and "mamífero" in list and "herbívoro" in list:
    print("vaca")
elif "invertebrado" in list and "inseto" in list and "hematófago" in list:
    print("pulga")
elif "invertebrado" in list and "inseto" in list and "herbívoro" in list:
    print("lagarta")
elif "invertebrado" in list and "anelídeo" in list and "hematófago" in list:
    print("sanguessuga")
elif "invertebrado" in list and "anelídeo" in list and "onívoro" in list:
    print("minhoca")

#Exercício 4
DDD = [61,71,11,21,32,19,27,31]
Destinos = ["Brasília", "Salvador", "São Paulo", 
            "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitória", "Belo Horizonte"]
ddd= int(input("Digite o DDD: "))
if ddd in DDD:
    indice = DDD.index(ddd)
    print("O DDD", ddd,"corresponde à: ",Destinos[indice])
else:
    print("DDD não cadastrado")

#Exercício 5
X, Y = map(int, input("Digite a Largura e a Altura: ").split())
if 0 <= X <= 432 and 0 <= Y <= 468:
    print("dentro")
else:
    print("fora")

#Exercício 6
A1 = int(input("Valor 1: "))
A2 = int(input("Valor 2: "))
A3 = int(input("Valor 3: "))
tempo_andar1 = 0*A1 + 2*A2 + 4*A3
tempo_andar2 = 2*A1 + 0*A2 + 2*A3
tempo_andar3 = 4*A1 + 2*A2 + 0*A3
menor_tempo = min(tempo_andar1, tempo_andar2, tempo_andar3)
print(menor_tempo)

#Exercício 7
for c in range(2,101,2):
    print(c)

#Exercício 8
maior = -1
posicao = 0
for i in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posicao = i

print(maior)
print(posicao)

#Exercício 9 
N = int(input("Digite a quantidade de passos: "))
contC = 0
contR = 0
contS = 0
contTotal=0
for c in range (N):
    entrada = input("Digite a quantidade de cobaias e em seguida o seu tipo: ")
    qnt, tipo = entrada.split()
    qnt= int(qnt)
    contTotal+=qnt
    if tipo in "Cc":
        contC+= qnt
    elif tipo in "Rr":
        contR+= qnt
    elif tipo in "Ss": 
        contS+= qnt
print("Total: ",contTotal)
print("Total de coelhos: ",contC)
print("Total de ratos: ",contR)
print("Total de sapos: ",contS)
Percentual_total= contC+contR+contS
Percentual_coelhos = (100*contC)/Percentual_total
Percentual_Ratos = (100*contR)/Percentual_total
Percentual_sapos= (100 * contS) / Percentual_total
print("Percentual de coelhos: ","{:.2f}".format(Percentual_coelhos))
print("Percentual de Ratos: ","{:.2f}".format(Percentual_Ratos))
print("Percentual de sapos: ","{:.2f}".format(Percentual_sapos))

#Exercício 10 
num = 0 
while num != 2002:
    num = int(input("Digite a senha: "))
    if num != 2002:
        print("Senha inválida")
print("Acesso Permitido")

#Exercício 11
N = int(input("Número: "))
for _ in range(N):
    X, Y = map(int, input().split()) 
    if Y == 0:
        print("divisao impossivel")
    else:
        resultado = X / Y 
        print(f"{resultado:.1f}")  

#Exercício 12
N = int(input("Digite um número: "))  
fibonacci = [0, 1]
for i in range(2, N):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
print(*fibonacci[:N])
    



    

    



