carros = ['Fusca', 'Civic', 'Palio', 'Corsa', 'Gol']

# Exibir o ultimo elemento da lista
print(carros[-1].title())

#Contatenar duas strings
print("O " + carros[0].title() + " é o carro mais bonito do mundo!")

# Alterar o primeiro elemento da lista
carros[0] = 'Fusca 1970'
print(carros)

# Adicionar um elemento no final da lista
carros.append('Civic 2020')
print(carros)

# Adicionar um elemento em uma posição específica
carros.insert(0, 'Fusca 1910')
print(carros)

#Outra forma de adicionar um elemento em uma posição específica
carros.extend(['Fusca 1910', 'Fusca 1910'])

# Remover um elemento específico da lista
del carros[0]
print(carros)

# Remover o último elemento da lista
carros.pop()
print(carros)

# Remover um elemento pelo seu valor
carros.remove('Fusca 1910')
print(carros)

# Inserir um elemento em uma posição específica
carros.insert(0, 'Fusca 1910')
print(carros)

# Inverter a lista 
print(sorted(carros))

# Reverter a lista
carros.reverse()
print(carros)