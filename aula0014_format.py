fn = "Jonathan"
ln = "Miranda"
idade = 31.9

# podemos utilizar nomes
frase = "b={nome2} a={nome1} a={nome1} c={info:.2f}"

formato = frase.format(nome1=fn, nome2=ln, info=idade)

print(formato)

# podemos utilizar indices
frase_2 = "b={1} a={0} c={2:.2f}"

formato_2 = frase_2.format(fn, ln, idade)

print(formato_2)
