carros = ['ferrari', 'civic', 'palio', 'corsa', 'gol']

# Listar item a item
for carro in carros:
    print("Eu quero um " + carro + "!")

print('Legal, né?')

# Listar números de 1 a 10
numeros = list(range(1, 11))
for n in numeros:
    print(n)

for n in range(1, 11):
    numeros.append(n)

print(numeros)