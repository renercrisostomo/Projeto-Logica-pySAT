from pysat.solvers import Glucose3
from pysat.formula import IDPool
from pysat.formula import CNF

def solve_tower_defense(r, s, mapa):
    num_torres = 0
    torres = []
    atacantes = []
    clauses = []
    
    formula = CNF()
    formulas = CNF()
    gerenciador = IDPool()
    formula_solver = Glucose3()

    # Percorre o mapa e coleta informações sobre torres e atacantes
    for i in range(r):
        for j in range(s):
            cell = mapa[i][j]
            if cell == 'T':
                num_torres += 1
                torres.append((i, j))
            elif cell == 'n':
                atacantes.append((i, j))

    # Cria as variáveis proposicionais para representar as orientações dos canhões
    variables = []
    variable = []
    for i in range(num_torres):
        for j in range(4):
            variable.append(gerenciador.id(f"t{i+1}_{j+1}"))
            variables.append(f"t{i+1}_{j+1}")
    formula.append(variable)

    # Restrição 1: Cada atacante pelo menos uma das torres que podem eliminá-lo
    for atacante in atacantes:
        atacante_row, atacante_col = atacante
        clause = []
        claus = []
        for i, torre in enumerate(torres):
            torre_row, torre_col = torre
            if (torre_row == atacante_row or torre_col == atacante_col):
                # Adiciona a cláusula que representa que a torre pode eliminar o atacante
                for j in range(4):
                    clause.append(variables[i * 4 + j])
                    claus.append(gerenciador.id(variables[i * 4 + j]))
        formulas.append(claus)
        clauses.append(clause)
    print(clauses)


    # Restrição 2: As torres não podem ser destruídas por outras torres
    for i, torre1 in enumerate(torres):
        torre1_row, torre1_col = torre1
        for j, torre2 in enumerate(torres):
            torre2_row, torre2_col = torre2
            if i != j and (torre1_row == torre2_row or torre1_col == torre2_col):
                # Adiciona a cláusula que representa que a torre1 não pode ser destruída por torre2
                for k in range(4):
                    clauses.append(["-" + variables[i * 4 + k], "-" +variables[j * 4 + k]])
                    formulas.append([-gerenciador.id(variables[i * 4 + k]), -gerenciador.id(variables[j * 4 + k])])
                    
    formula_solver.append_formula(formulas)
    
    # Verifica a satisfatibilidade das cláusulas
    if formula_solver.solve():
        # Se for satisfatível, obtém a valoração das variáveis proposicionais
        model = formula_solver.get_model()
        form = []
        for literal in model:
            if literal > 0:
                form.append(gerenciador.obj(literal))
            elif literal < 0:
                form.append("-" + gerenciador.obj(-literal))
        orientacoes = {}
        for variable in form:
            variable_name = variable.strip('-')
            partes = variable_name.split("_")
            torre_idx = int(partes[0][1:])
            orientacao = int(partes[1])
            orientacoes[torre_idx] = orientacao
            
        # Gera o mapa com as orientações dos canhões
        for i, torre in enumerate(torres):
            torre_row, torre_col = torre
            orientacao = orientacoes[i + 1]
            if orientacao == 1:
                mapa[torre_row][torre_col] = '1'
            elif orientacao == 2:
                mapa[torre_row][torre_col] = '2'
            elif orientacao == 3:
                mapa[torre_row][torre_col] = '3'
            elif orientacao == 4:
                mapa[torre_row][torre_col] = '4'

        return mapa
    else:
        return None

# Exemplo de uso
with open("input.txt", "r") as f:
    arquivo = list(linha.split() for linha in f.readlines())
    for i in arquivo:
        print(''.join(i))
    r, s = map(int, arquivo[0])
    mapa = [list(*linha) for linha in arquivo[1:]]
    f.close()

print("\nResolvendo o problema...\n")

solucao = solve_tower_defense(r, s, mapa)

if solucao is None:
    print("Não é possível configurar os canhões para satisfazer as condições do jogo.")
else:
    for linha in solucao:
        print(''.join(linha))
