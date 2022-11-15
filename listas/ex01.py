# 1-> Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numeros = []
num = int(input("Informe o tamanho dad lista:"))
for i in range(num):
    numeros.append(input(str(i+1) + "° Número: "))
numeros.sort(reverse=True)  # mostre-os na ordem inversa.
print("Ordem inversa: ", numeros)
numeros.sort()  # mostre-os na forma ordenada.
print("Números ordenados: ", numeros)
