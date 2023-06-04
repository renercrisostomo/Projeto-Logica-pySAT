with open("input.txt", "r") as f:
    arquivo = list(linha.split() for linha in f.readlines())
    for i in arquivo:
        print(i)
    linhas, colunas = map(int, arquivo[0])
    mapa = [list(*linha) for linha in arquivo[1:]]
    f.close()

def torreEsquerda(linha, coluna):
    if coluna == 0:
        return False
    else:
        for indice in range(coluna - 1, -1, -1):
            if mapa[linha][indice] == "#":
                return False
            elif mapa[linha][indice] == "T":
                return True
    return False
            
def torreDireita(linha, coluna):
    if coluna == colunas - 1:
        return False
    else:
        for indice in range(coluna + 1, colunas):
            if mapa[linha][indice] == "#":
                return False
            elif mapa[linha][indice] == "T":
                return True
    return False
            
def torreCima(linha, coluna):
    if linha == 0:
        return False
    else:
        for indice in range(linha - 1, -1, -1):
            if mapa[indice][coluna] == "#":
                return False
            elif mapa[indice][coluna] == "T":
                return True
    return False
            
def torreBaixo(linha, coluna):
    if linha == linhas - 1:
        return False
    else:
        for indice in range(linha + 1, linhas):
            if mapa[indice][coluna] == "#":
                return False
            elif mapa[indice][coluna] == "T":
                return True
    return False

Restricoes = []
torres = 0
for linha in mapa:
    for elemento in linha:
        if elemento == "T":
            logicaT = []
            torres += 1
            logicaOrtogonal = ["Ortagonais"] #Adicionar restrições para tiros Ortagonais
            Restricoes.append(logicaOrtogonal)
            linhaT = mapa.index(linha)
            colunaT = linha.index(elemento)
            if not torreEsquerda(linhaT, colunaT): logicaT.append(f"T{torres}e")
            if not torreDireita(linhaT, colunaT): logicaT.append(f"nT{torres}e")
            if not torreCima(linhaT, colunaT): logicaT.append(f"T{torres}c")
            if not torreBaixo(linhaT, colunaT): logicaT.append(f"nT{torres}c")
            Restricoes.append(logicaT)
        
            
for i in mapa:
    print(i)
for i in Restricoes:
    print(i)



with open("output.txt", "w") as f:
    for linha in mapa:
        for elemento in linha:
            f.write(elemento)
        f.write("\n")
    f.close()
    