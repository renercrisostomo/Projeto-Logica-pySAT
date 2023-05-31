with open("input.txt", "r") as f:
    arquivo = [linha.replace("\n", "").split() for linha in f.readlines()]
    linhas, colunas = map(int, arquivo[0])
    mapa = arquivo[1:]
    f.close()

indices = []
for linha in range(len(mapa)):
    indices.append([indice for indice, elemento in enumerate(mapa[linha]) if elemento == "T"])

with open("output.txt", "w") as f:
    for linha in mapa:
        f.write(" ".join(linha) + "\n")
    for linha in indices:
        f.write(" ".join(linha) + "\n")
    f.close()

