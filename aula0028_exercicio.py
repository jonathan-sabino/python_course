"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
user_name = input("Digite seu nome: ")
user_age = input("Digite sua idade: ")

if not user_name or not user_age:
    print("Desculpe, você deixou campos vazios. Preencha novamente!")
    user_name = input("Digite seu nome: ")
    user_age = input("Digite sua idade: ")
else:
    print(f"Seu nome é {user_name}")
    print(f"Seu nome invertido é {user_name[::-1]}")

    if " " in user_name:
        print("Seu nome contém espaços")
    else:
        print("Seu nome NÃO contém espaços")

    print(f"Seu nome contém {len(user_name)} letras")
    print(f"A primeira letra do seu nome é {user_name[0]}")
    print(f"A última letra do seu nome é {user_name[-1]}")
