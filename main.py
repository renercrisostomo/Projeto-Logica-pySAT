with open("input.txt", "r") as f:
    arquivo = [linha.replace("\n", "").split() for linha in f.readlines()]
    linhas, colunas = map(int, arquivo[0])
    mapa = arquivo[1:]
    f.close()

with open("output.txt", "w") as f:
    for linha in mapa:
        f.write(" ".join(linha) + "\n")
    f.close()

