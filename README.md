# Projeto Logica pySAT

Repositório do projeto da disciplina Lógica para computação do 4º semestre do curso ciências da computação do IFCE Maracanaú

- Projeto prático em dupla para resolver o jogo Defesa com Torres usando pySAT
- O jogo consiste em defender-se de atacantes usando torres com canhões em uma grade retangular
- Cada torre tem dois canhões que devem ser posicionados em ângulos de 90° ((cima ou baixo) e (esquerda ou direita))
- A entrada é um mapa do jogo com as dimensões da grade e os elementos do jogo
    1. "T" - Torres (devem ser defendidas)
    2. "n" - Atacantes (devem ser atacados, mas não param a bala dos canhões)
    3. "#" - Obstáculos (não é destruído e consegue parar a bala dos canhões)
- A saída é o mapa com as orientações dos canhões nas torres
    1. "1" - Canhão virado para a esquerda e para baixo
    2. "2" - Canhão virado para a direita e para baixo
    3. "3" - Canhão virado para a direita e para cima
    4. "4" - Canhão virado para a esquerda e para cima

## Exemplos

### Exemplo 1

Entrada

```txt
5 9
.n..T..n.
.T..n....
.n..#..n.
....n..T.
.n..T..n.
```

Saída

```txt
.n..4..n.
.2..n....
.n..#..n.
....n..4.
.n..3..n.
```

### Exemplo 2

Entrada

```txt
9 13
.............
...........n.
.n.T..nnnn#..
.............
.T#n..n....T.
.............
.n.T..T....n.
.............
......n......
```

Saída

```txt
.............
...........n.
.n.3..nnnn#..
.............
.4#n..n....4.
.............
.n.1..2....n.
.............
......n......
```

### Exemplo 3

Entrada

```txt
9 8
n.Tnnnnn
nnnnnnTn
nTnnnnnn
nnnnTnnn
Tnnnnnnn
..#nnTnn
nnnnnnnT
nnnTn.n.
.nTnnnnn
```

Saída

```txt
n.3nnnnn
nnnnnn1n
n2nnnnnn
nnnn1nnn
3nnnnnnn
..#nn4nn
nnnnnnn4
nnn4n.n.
.n3nnnnn
```
