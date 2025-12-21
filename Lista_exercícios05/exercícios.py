#Exercício 1
def Maior(a, b):
    return a if a > b else b

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior_valor = Maior(valor1, valor2)
print(f"O maior valor entre {valor1} e {valor2} é: {maior_valor}")

#Exercício 2
def MaiorDeTres(a, b, c):
    list = [a,b,c]
    return max(list)

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

maior_valor = MaiorDeTres(valor1, valor2, valor3)
print(f"O maior valor entre {valor1}, {valor2} e {valor3} é: {maior_valor}")

#Exercício 3
def Iniciais(nome_completo):
    partes = nome_completo.split()
    iniciais = ''
    for parte in partes:
        iniciais += parte[0].upper()
    return iniciais

nome = input("Digite seu nome completo: ")
iniciais = Iniciais(nome)
print(f"As iniciais do nome '{nome}' são: {iniciais}")

#Exercício 4
def Aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media >= 60

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))

if Aprovado(nota1, nota2):
    print("O aluno foi aprovado.")
else:
    print("O aluno está em prova final.")

#Exercício 5
def formatar_nome(nome_completo):
    return nome_completo.title()

nome = input("Digite seu nome completo: ")
print(f"Nome formatado: {formatar_nome(nome)}")
