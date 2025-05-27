escreva = ''

while escreva != 'sair':
    print("Caso queira sair, digite 'sair'.\n")
    escreva = input('Escreva algo: ')
    print(escreva)

    if escreva == 'continuar':
        continue
    elif escreva == 'sair':
        print('Saindo do programa...')
        break
    else:
        print('Continuando o programa...')

print('Programa encerrado.')