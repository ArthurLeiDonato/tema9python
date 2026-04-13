# Solicita o nome completo
nome = input("Digite seu nome completo: ")

# 1. Quantidade de caracteres (incluindo espaços)
quantidade = len(nome)

# 2. Primeira letra
primeira_letra = nome[0]

# 3. Última letra
ultima_letra = nome[-1]

# 4. Nome em maiúsculas
nome_maiusculo = nome.upper()

# Exibição dos resultados
print("Quantidade de caracteres:", quantidade)
print("Primeira letra:", primeira_letra)
print("Última letra:", ultima_letra)
print("Nome em maiúsculas:", nome_maiusculo)