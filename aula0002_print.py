# \r\n -> CRLF carriage return line-feed
# (usado por linguagens e sistemas mais antigos)
# \n -> LF (simplificação do \r\n)
# sep = separador (por padrão " " <espaço>)
# end = terminador (por padrão \n <quebra de linha>)
print(12, 34, 1011, sep="", end="#")
print(56, 78, sep="-", end="\n")
print(9, 10, sep="-", end="\n")
