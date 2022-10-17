# A funcao colon recebe uma string e retorna uma
# string com ponto e virgula no lugar das virgulas,
# exceto as virgulas entre aspas.

def colon(fline):
  colon = ''
  n = len(fline)
  for i in range(n):
    if (fline[i] != ','):
      colon += fline[i]
    if (fline[i] == ','):
      colon += ';'
    i += 1
    
  n = len(fline)
  quote = []
  j = 0
  for i in range(n):
    if (fline[i] == '"'):
      quote.append(i)
      j += 1
    i += 1

  linha = list(colon)
  m = len(quote)
  j = 0
  while (j < m):
    i = quote[j]
    while i < quote[j+1] :
      linha[i] = fline[i]
      i += 1
    j += 2
  linha = ''.join(linha)
  return(linha)

# f abre o arquivo "arquivo_dados.txt"
f = open("arquivo_dados.txt","r")

# g cria o arquivo "pontoevirgula.txt"
g = open("pontoevirgula.txt","x")
g.close()

# h abre "pontoevirgula.txt" e permite
# adicionar linhas ao arquivo com "a"
h = open("pontoevirgula.txt","a")

for a in f:
  # string linha1 recebe linhas de "arquivo_dados.txt" 
  linha1 = f.readline()

  # linha2 = linha1 com ',' trocada por ';'
  linha2 = colon(a)

  # h adiciona linha2 ao arquivo "pontoevirgula.txt"
  h.write(linha2)

# Arquivos sao fechados
f.close()
h.close()
