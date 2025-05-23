# verificar se tem permissão para votar
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

#menor de 16 anos não pode votar
#maior de 16 anos pode votar, mas não é obrigatório
#entre 18 anos e 65 votar é obrigatório

idade = int(idade)  # Convert input to integer

if idade < 16:
    print(f"{nome}, você tem {idade} anos e não pode votar.")
elif (idade >= 16 and idade < 18) or (idade > 64):
    print(f"{nome}, você tem {idade} anos e pode votar, mas não é obrigatório.")
else:
    print(f"{nome}, você tem {idade} anos e é obrigatório votar.")

# O "f" em f-strings é usado para formatar strings em Python, permitindo inserir variáveis dentro de strings