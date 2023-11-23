"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_agora = input("Informe a hora sem os minutos, utilizando apenas números: ")


try:
    hora_agora_int = int(hora_agora)

    if hora_agora_int >= 0 and hora_agora_int <= 11:
        print("Bom dia!")
    elif hora_agora_int >= 11 and hora_agora_int <= 17:
        print("Boa tarde!")
    else:
        print("Boa noite!")
except:
    print("hora digitada no formato inválido!")
