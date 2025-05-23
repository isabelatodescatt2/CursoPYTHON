cor = "azul"
if cor == "roxo":
    print(cor)

elif cor == "azul":
    print(cor)

else:
    print("não é roxo nem azul") 

# ----------------------------------------------------------------------------
# levar em conta a identação - ordem de elemeentos
# ----------------------------------------------------------------------------

num = 0 
if num == 1:
    if cor == "roxo":
        print(cor)

    elif cor == "azul":
        print(cor)

    else:
        print("não é roxo nem azul") 
    
else:
    print("não é 1")

# ----------------------------------------------------------------------------

carros = ['audi', 'bmw', 'mercedes', 'ferrari', 'porsche']

for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    else:
        print(carro.title())

