ingred_pedido = []
continuar = "s"

while continuar.lower() == "s":  

    ing = input("Digite o ingrediente que deseja adicionar ao lanche: ")
    ingred_pedido.append(ing.lower())  
    continuar = input("Deseja adicionar mais ingredientes? (s/n): ")


#ingredientes da hamburgueria
ingredientes = ['mostarda', 'maionese', 'ketchup', 'picles', 'cebola', 'alface', 'tomate', 'queijo', 'hamburguer']


# verifica se o ingrediente está na lista de ingredientes
# e adiciona ao lanche
lanche = []
for ingrediente in ingred_pedido:
    
    if ingrediente in ingredientes:
        lanche.append(ingrediente)
    else:
        print ("Sinto muito, mas não temos " + ingrediente + " no momento")
        

print("\nSeu lanche contém os seguintes ingredientes: ")
for ing in lanche:
    print (ing)
