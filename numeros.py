soma = 2 + 3
subtracao = 3 - 2
mult = 2 * 3
div = 3 / 2
exp = 2 ** 3

print("Soma: " + str(soma))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(mult))
print("Divisão: " + str(div))
print("Exponenciação: " + str(exp))

oper = (2 + 3) * 4
print("Operação: " + str(oper))

# ----------------------------------------------------------------------------
# Concatenando strings e inteiros

palavra = "Oi"
palavra2 = "Polera bobao! Você tem "
idade = 18
palavra3 = ", sua idade está certa?"

print(palavra + palavra2 + str(idade) + palavra3)
# O que acontece se não convertermos a variável idade para string?
# O programa não roda, pois não é possível concatenar uma string com um inteiro.