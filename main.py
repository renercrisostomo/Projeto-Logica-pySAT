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
#atacante = {}

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
                    #atacante[f'{linha} x {indice}'] = []
                atacantes[f'{linha} x {indice}'].append(gerenciador.id(f"T{torre}e"))
                #atacantes[f'{linha} x {indice}'].append(f"T{torre}e")
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
                    #atacante[f'{linha} x {indice}'] = []
                atacantes[f'{linha} x {indice}'].append(-gerenciador.id(f"T{torre}e"))
                #atacantes[f'{linha} x {indice}'].append(f"nT{torre}e")
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
                    #atacante[f'{indice} x {coluna}'] = []
                atacantes[f'{indice} x {coluna}'].append(gerenciador.id(f"T{torre}c"))
                #atacantes[f'{indice} x {coluna}'].append(f"T{torre}c")
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
                    #atacante[f'{indice} x {coluna}'] = []
                atacantes[f'{indice} x {coluna}'].append(-gerenciador.id(f"T{torre}c"))
                #atacantes[f'{indice} x {coluna}'].append(f"nT{torre}c")
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
            possibilidade.append(gerenciador.id(f"T{contTorres}e"))
            possibilidade.append(-gerenciador.id(f"T{contTorres}e"))
            possibilidade.append(gerenciador.id(f"T{contTorres}c"))
            possibilidade.append(-gerenciador.id(f"T{contTorres}c"))
            formula.append(possibilidade)
            Restricoes.append(["logicaOrtogonal"]) #Adicionar restrições para tiros Ortagonais
            linhaT = mapa.index(linha)
            colunaT = coluna
            if torreEsquerda(linhaT, colunaT, contTorres): 
                formulas.append([-gerenciador.id(f"T{contTorres}e")])
            if torreDireita(linhaT, colunaT, contTorres): 
                formulas.append([gerenciador.id(f"T{contTorres}e")])
            if torreCima(linhaT, colunaT, contTorres): 
                formulas.append([-gerenciador.id(f"T{contTorres}c")])
            if torreBaixo(linhaT, colunaT, contTorres):
                formulas.append([gerenciador.id(f"T{contTorres}c")])

for i in atacantes:
    #Restricoes.append(atacantes[i]) 
    formulas.append(atacantes[i])   

print("Mapa:")
for i in mapa:
    print(i)

print("Atacantes:")
for i in atacantes:
    print(i, end=" ")
    form = []
    for j in atacantes[i]:
        if j < 0:
            form.append(f"n{gerenciador.obj(-j)}")
        else:
            form.append(gerenciador.obj(j))
    print(form)


print("Formula Final:")
formulaFinal = []
for literal in formulas:
    form = []
    for j in literal:
        if j < 0:
            form.append(f"n{gerenciador.obj(-j)}")
        else:
            form.append(gerenciador.obj(j))
    formulaFinal.append(form)
print(formulaFinal)

print(formulas.clauses)

# Montagem das formulas em CNF para o pySAT

formula_solver.append_formula(formulas)

# print(formula_solver.solve())

if formula_solver.solve():
    print("Satisfatível")

    print("Modelo:")
    print(formula_solver.get_model())
    model = formula_solver.get_model()
    form = []
    for literal in model:
        if literal > 0:
            form.append(gerenciador.obj(literal))
        elif literal < 0:
            form.append(f"n{gerenciador.obj(-literal)}")
    print(form)
    
    orientacao_canhoes = []
    
    contTorre = 0
    for linha in mapa:
        for coluna, elemento in enumerate(linha):
            if elemento == "T":
                contTorre += 1
                linT = mapa.index(linha)
                colT = coluna
                orientação = {1: [f"T{contTorre}e", f"nT{contTorre}c"], 2: [f"nT{contTorre}e", f"nT{contTorre}c"], 3: [f"nT{contTorre}e", f"T{contTorre}c"], 4: [f"T{contTorre}e", f"T{contTorre}c"]}
                for torre in range(0, len(form), 2):
                    elemento1 = form[torre]
                    elemento2 = form[torre + 1] if torre + 1 < len(form) else None
                    if [elemento1, elemento2] == orientação[1] or [elemento2, elemento1] == orientação[1]:
                        print(f"torre {contTorre}: {linT} x {colT} = 1")
                        mapa[linT][colT] = '1'
                    elif [elemento1, elemento2] == orientação[2] or [elemento2, elemento1] == orientação[2]:
                        print(f"torre {contTorre}: {linT} x {colT} = 2")
                        mapa[linT][colT] = '2'
                    elif [elemento1, elemento2] == orientação[3] or [elemento2, elemento1] == orientação[3]:
                        print(f"torre {contTorre}: {linT} x {colT} = 3")
                        mapa[linT][colT] = '3'
                    elif [elemento1, elemento2] == orientação[4] or [elemento2, elemento1] == orientação[4]:
                        print(f"torre {contTorre}: {linT} x {colT} = 4")
                        mapa[linT][colT] = '4'

    # Ler a saida do pySAT e montar o mapa final
    with open("output.txt", "w") as f:
        for linha in mapa:
            for elemento in linha:
                f.write(elemento)
            f.write("\n")
        f.close()
else:
    print("Insatisfatível")
    with open("output.txt", "w") as f:
        f.write("Insatisfatível")
        f.close()
    