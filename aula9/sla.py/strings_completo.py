# Entrada do usuário
nome = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome}!")

# Mostrando cada caractere
print("\nCaracteres do seu nome:")
for i in range(len(nome)):
    print(f"Posição {i}: {nome[i]}")

# Invertendo a string
print(f"\nSeu nome invertido: {nome[::-1]}")