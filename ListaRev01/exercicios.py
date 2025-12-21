import calendar

# Exercício 1
def maior_ou_igual(a, b):
    if a > b:
        return f"Maior = {a}"
    elif b > a:
        return f"Maior = {b}"
    else:
        return "Números iguais"
    
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print(maior_ou_igual(a,b))

# Exercício 2
valores = [int(input()) for _ in range(4)]
media = sum(valores) / 4
print(f"Média = {media}")
print("Números menores que a média")
for v in valores:
    if v < media:
        print(v)
print("Números maiores ou iguais à média")
for v in valores:
    if v >= media:
        print(v)

#Exercício 3
valores = [int(input("Digite um número: ")) for _ in range(4)]
listP =[]
listI=[]
for v in valores:
    if v%2==0:
        listP.append(v)
    else:
        listI.append(v)
soma1 = sum(listP)
soma2 = sum(listI)
print("Soma dos pares: ", soma1)
print("Soma dos Ímpares: ", soma2)

#Exercício 4
h1, m1 = map(int, input("Digite o primeiro horário: ").split(":"))
h2, m2 = map(int, input("Digite o segundo horário: ").split(":"))
horas_totais = h1 + h2
minutos_totais = m1 + m2
if minutos_totais >= 60:
    horas_totais += minutos_totais // 60 
    minutos_totais = minutos_totais % 60  
print(f"Total de horas = {horas_totais:02}:{minutos_totais:02}")

#Exercício 5
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = input("Digite o mês: ").lower()  # Converter para minúsculas para evitar erro de case
if mes in meses:
    indice = meses.index(mes)
    trimestre = (indice) // 3 + 1
    print(f"O mês de {meses[indice]} é do {trimestre}º trimestre do ano")
else:
    print("Mês inválido!")

#Exercício 6
valores = [int(input()) for _ in range(3)]
soma = min(valores) + max(valores)
print(f"A soma do maior com o menor número é {soma}.")

#Exercício 7
import math
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Impossível calcular")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print(f"A raiz é {raiz1}")
    else:
        print(f"As raízes são {raiz1} e {raiz2}")

#Exercício 8
valores = [int(input("Digite um valor: ")) for _ in range(4)]
if len(set(valores)) != 4:
    print("Erro: os valores devem ser diferentes.")
else:
    valores.sort()
    maior = valores[-1]
    menor = valores[0]
    segundo_maior = valores[-2]
    segundo_menor = valores[1]

    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    print(f"A soma do segundo maior valor com o segundo menor = {segundo_maior + segundo_menor}")

#Exercício 9
def calcular_angulo(hora, minuto):
    if hora < 0 or hora > 12 or minuto < 0 or minuto > 59:
        return "Hora Inválida"
    angulo_horas = 30 * hora + 0.5 * minuto 
    angulo_minutos = 6 * minuto  
    angulo = abs(angulo_horas - angulo_minutos)
    if angulo > 180:
        angulo = 360 - angulo       
    return f"Menor ângulo entre os ponteiros = {angulo} graus"
hora, minuto = map(int, input("Digite o horário no formato hh:mm: ").split(":"))
resultado = calcular_angulo(hora, minuto)
print(resultado)

#Exercício 10
def validar_data(data):
    dia, mes, ano = map(int, data.split("/"))

    if not (1900 <= ano <= 2100): return "A data informada não é válida"
    if not (1 <= mes <= 12): return "A data informada não é válida"
    dias_por_mes = [31, 28 + (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= dia <= dias_por_mes[mes - 1]): return "A data informada não é válida"
    
    return "A data informada é válida"

data = input("Digite uma data no formato dd/mm/aaaa: ")
print(validar_data(data))

#Exercício 11
def formatar_data(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", 
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dia, mes, ano = data.split("/")
    return f"A data é {dia} de {meses[int(mes) - 1]} de {ano}"
data = input("Digite uma data no formato dd/mm/aaaa: ")
print(formatar_data(data))

#Exercício 12
def calcular_operacao(expressao):
    for operador in ["+", "-", "*", "/"]:
        if operador in expressao:
            numero1, numero2 = expressao.split(operador)
            numero1, numero2 = int(numero1), int(numero2)
            if operador == "+":
                return f"O resultado da operação é {numero1 + numero2}"
            elif operador == "-":
                return f"O resultado da operação é {numero1 - numero2}"
            elif operador == "*":
                return f"O resultado da operação é {numero1 * numero2}"
            elif operador == "/":
                if numero2 != 0:
                    return f"O resultado da operação é {numero1 / numero2}"
                else:
                    return "Não é possível dividir por zero"
    return "Operação inválida"
expressao = input("Digite dois valores inteiros separados por um operador +, -, * ou /: ")
print(calcular_operacao(expressao))

#Exercício 13
numeros = list(map(int, input("Digite dez valores inteiros: ").split()))
maior = max(numeros)
menor = min(numeros)
print(f"O maior valor é {maior} e o menor é {menor}")

#Exercício 14 
def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triângulo equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Esses valores não formam um triângulo"
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
print(tipo_triangulo(a, b, c))

#Exercício 15 
valores = [int(input("Digite um valor: ")) for _ in range(3)]
valores.sort()
print(f"Os valores em ordem crescente são: {valores[0]}, {valores[1]} e {valores[2]}")

