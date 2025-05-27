def animais(especie, nome):
    especie = especie
    nome = nome.title()
    print("Eu tenho um(a) " + especie + " chamado " + nome + ".")

# Exemplo de chamada da função em diferentes ordens, mas mesmo resultado
animais(nome='charlie', especie='gato')
animais('gato', 'lola')

# ----------------------------------------------------------------------------

def nome_completo(primeiro_nome="", ultimo_nome="", nome_do_meio=""):
    primeiro_nome = primeiro_nome.title()
    nome_do_meio = nome_do_meio.title()
    ultimo_nome = ultimo_nome.title()

    if nome_do_meio != "":
        print("Seu nome completo é " + primeiro_nome + " " + nome_do_meio + " " + ultimo_nome + ".")

    else:
        print("Seu nome completo é " + primeiro_nome + " " + ultimo_nome + ".")

print(nome_completo("cleubis", "lima", "de souza"))
print(nome_completo("cleubis", "de souza"))
