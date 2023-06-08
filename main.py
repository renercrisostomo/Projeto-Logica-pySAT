from pysat.solvers import Glucose3
from pysat.formula import IDPool
from pysat.formula import CNF

# Importações

with open("input.txt", "r") as f:
    arquivo = list(linha.split() for linha in f.readlines())
    for i in arquivo:
        print(i)
    linhas, colunas = map(int, arquivo[0])
    mapa = [list(*linha) for linha in arquivo[1:]]
    f.close()

formulas = CNF()
formula = CNF()
gerenciador = IDPool()
formula_solver = Glucose3()

atacantes = {}
atacante = {}

def torreEsquerda(linha, coluna, torre):
    if coluna == 0:
        return False
    else:
        for indice in range(coluna - 1, -1, -1):
            if mapa[linha][indice] == "#":
                return False
            elif mapa[linha][indice] == "T":
                return True
            elif mapa[linha][indice] == "n":
                if f'{linha} x {indice}' not in atacantes:
                    atacantes[f'{linha} x {indice}'] = []
                    atacante[f'{linha} x {indice}'] = []
                atacante[f'{linha} x {indice}'].append(gerenciador.id(f"T{torre}e"))
                atacantes[f'{linha} x {indice}'].append(f"T{torre}e")
    return False
            
def torreDireita(linha, coluna, torre):
    if coluna == colunas - 1:
        return False
    else:
        for indice in range(coluna + 1, colunas):
            if mapa[linha][indice] == "#":
                return False
            elif mapa[linha][indice] == "T":
                return True
            elif mapa[linha][indice] == "n":
                if f'{linha} x {indice}' not in atacantes:
                    atacantes[f'{linha} x {indice}'] = []
                    atacante[f'{linha} x {indice}'] = []
                atacante[f'{linha} x {indice}'].append(-gerenciador.id(f"T{torre}e"))
                atacantes[f'{linha} x {indice}'].append(f"nT{torre}e")
    return False
            
def torreCima(linha, coluna, torre):
    if linha == 0:
        return False
    else:
        for indice in range(linha - 1, -1, -1):
            if mapa[indice][coluna] == "#":
                return False
            elif mapa[indice][coluna] == "T":
                return True
            elif mapa[indice][coluna] == "n":
                if f'{indice} x {coluna}' not in atacantes:
                    atacantes[f'{indice} x {coluna}'] = []
                    atacante[f'{indice} x {coluna}'] = []
                atacante[f'{indice} x {coluna}'].append(gerenciador.id(f"T{torre}c"))
                atacantes[f'{indice} x {coluna}'].append(f"T{torre}c")
    return False
            
def torreBaixo(linha, coluna, torre):
    if linha == linhas - 1:
        return False
    else:
        for indice in range(linha + 1, linhas):
            if mapa[indice][coluna] == "#":
                return False
            elif mapa[indice][coluna] == "T":
                return True
            elif mapa[indice][coluna] == "n":
                if f'{indice} x {coluna}' not in atacantes:
                    atacantes[f'{indice} x {coluna}'] = []
                    atacante[f'{indice} x {coluna}'] = []
                atacante[f'{indice} x {coluna}'].append(-gerenciador.id(f"T{torre}c"))
                atacantes[f'{indice} x {coluna}'].append(f"nT{torre}c")
    return False

Restricoes = []
contTorres = 0
for linha in mapa:
    for coluna, elemento in enumerate(linha):
        if elemento == "T":
            contTorres += 1 
            logicaT = []
            logicaT_teste = []
            possibilidade = []
            possibilidade_teste = []
            possibilidade.append(gerenciador.id(f"T{contTorres}e"))
            possibilidade_teste.append(f"T{contTorres}e")
            possibilidade.append(-gerenciador.id(f"T{contTorres}e"))
            possibilidade_teste.append(f"nT{contTorres}e")
            possibilidade.append(gerenciador.id(f"T{contTorres}c"))
            possibilidade_teste.append(f"T{contTorres}c")
            possibilidade.append(-gerenciador.id(f"T{contTorres}c"))
            possibilidade_teste.append(f"nT{contTorres}c")
            formula.append(possibilidade)
            # Restricoes.append(["logicaOrtogonal"]) #Adicionar restrições para tiros Ortagonais
            linhaT = mapa.index(linha)
            colunaT = coluna
            if not torreEsquerda(linhaT, colunaT, contTorres): 
                logicaT.append(gerenciador.id(f"T{contTorres}e"))
                logicaT_teste.append(f"T{contTorres}e")
            if not torreDireita(linhaT, colunaT, contTorres): 
                logicaT.append(-gerenciador.id(f"T{contTorres}e"))
                logicaT_teste.append(f"nT{contTorres}e")
            if not torreCima(linhaT, colunaT, contTorres): 
                logicaT.append(gerenciador.id(f"T{contTorres}c"))
                logicaT_teste.append(f"T{contTorres}c")
            if not torreBaixo(linhaT, colunaT, contTorres):
                logicaT.append(-gerenciador.id(f"T{contTorres}c"))
                logicaT_teste.append(f"nT{contTorres}c")
            #Restricoes.append(logicaT)
            Restricoes.append(logicaT_teste)
            formulas.append(logicaT)
for i in atacantes:
    Restricoes.append(atacantes[i]) 
    formulas.append(atacante[i])   

print("Mapa:")
for i in mapa:
    print(i)

print("Atacantes:")
for i in atacantes:
    print(i, atacantes[i])

print("Restrições Finais:")
for i in Restricoes:
    print(i)

print(formulas.clauses)

# Montagem das formulas em CNF para o pySAT

formula_solver.append_formula(formulas)

print(formula_solver.solve())
print(formula_solver.get_model())

model = formula_solver.get_model()
form = []
for literal in model:
    if literal > 0:
        form.append(gerenciador.obj(literal))
    elif literal < 0:
        form.append(f"n{gerenciador.obj(-literal)}")
print(form)

# Ler a saida do pySAT e montar o mapa final
with open("output.txt", "w") as f:
    for linha in mapa:
        for elemento in linha:
            f.write(elemento)
        f.write("\n")
    f.close()
    