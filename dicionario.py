invasor_zim = {'cor': 'verde', 'pontuacao': 5}

print(invasor_zim['cor'])

invasor_zim['cor'] = 'roxo'

print(invasor_zim['cor'])
print(invasor_zim['pontuacao'])

invasor_zim['pontuacao'] = 10

print("O Invasor Zim tem agora " + str(invasor_zim['pontuacao']) + " pontos.")

print(invasor_zim)

invasor_zim['posicao_x'] = 0
invasor_zim['posicao_y'] = 25
print(invasor_zim)