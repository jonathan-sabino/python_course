"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
user_name = input("Digite seu nome: ")
len_user_name = len(user_name)

if len_user_name <= 4:
    print(f"{user_name} é um nome curto!")
elif len_user_name >= 5 and len_user_name <= 6:
    print(f"{user_name} é um nome normal!")
else:
    print(f"{user_name} é um nome longo!")
