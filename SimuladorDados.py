import random

def rolar_dado():
    return random.randint(1, 6)

while True:
    input("Pressione Enter para rolar o dado...")
    print(f"Você rolou um {rolar_dado()}!")
    continuar = input("Deseja jogar novamente? (s/n): ").lower()
    if continuar != 's':
        break