""" exercício """
primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior ou igual " f"ao que {segundo_valor=}")
elif primeiro_valor < segundo_valor:
    print(f"{segundo_valor=} é maior " f"do que {primeiro_valor=}")
else:
    print(f"{primeiro_valor=} é igual " f"ao {segundo_valor=}")
