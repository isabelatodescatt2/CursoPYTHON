lista_cor = ["roxo", "azul", "rosa", "branco", "preto"]
print(lista_cor)

def lista_funcao(lista):
    for cor in lista:
        print(cor)
        lista.pop()

lista_funcao(lista_cor[:])
print(lista_cor)