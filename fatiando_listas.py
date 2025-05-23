alimentos = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi']

#pegar os elementos de 3 à 5
print(alimentos[2:5])

#pegar elemnto inicial de dois em dois
print(alimentos[::2])

#pegar os três ultimos elementos
print(alimentos[-3:])

#pegar os elementos de 3 à 5
for alimento in alimentos[:3]:
    print(alimento.title())

