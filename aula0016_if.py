# if / elif / else

entrada = input("Você quer entrar ou sair? ")

# if pode estar sozinho, mas elif e else não
# podemos ter quantos elif for necessários
# porém é importante lembrar que a estrutura de código
# para de ser executada ao encontrar a primeira condição true
if entrada == "entrar":
    print("Você entrou no sistema!")
elif entrada == "sair":
    print("Você saiu do sistema!")
else:
    print("Você não digitou nem entrar e nem sair!")

print("Fora dos blocos!")
