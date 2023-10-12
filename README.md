# Projeto Lógica pySAT

Repositório do projeto da disciplina Lógica para Computação do 4º semestre do curso Ciências da Computação do IFCE Maracanaú

## Sobre o Projeto

O objetivo deste projeto é utilizar a biblioteca pySAT, uma ferramenta Python para resolver problemas de satisfatibilidade proposicional (SAT), para resolver o jogo Defesa com Torres, um jogo de estratégia em que você deve posicionar canhões nas torres para defender-se dos atacantes que se aproximam em uma grade retangular.

O jogo Defesa com Torres funciona da seguinte forma:

- A grade retangular tem dimensões M x N, onde M é o número de linhas e N é o número de colunas.
- A grade contém elementos do jogo, representados por caracteres, que podem ser:
    - "T" - Torres: são as estruturas que devem ser defendidas dos atacantes. Cada torre tem dois canhões que devem ser posicionados formando ângulos de 90° entre si. Os canhões disparam balas que podem atingir os atacantes, mas também podem ser bloqueadas por obstáculos.
    - "n" - Atacantes: são os inimigos que devem ser eliminados pelos canhões das torres. Os atacantes não param a bala dos canhões, ou seja, a bala pode atravessar vários atacantes até encontrar um obstáculo ou sair da grade.
    - "#" - Obstáculos: são elementos que não são destruídos e conseguem parar a bala dos canhões. Os obstáculos podem ser usados para proteger as torres ou dificultar o alcance dos atacantes.
- A entrada do jogo é um mapa com as dimensões da grade e os elementos do jogo, representados por caracteres. Por exemplo:

```txt
5 9
.n..T..n.
.T..n....
.n..#..n.
....n..T.
.n..T..n.
```

- A saída do jogo é um mapa com as orientações dos canhões nas torres, representadas por números. As orientações dos canhões são:
    - "1" - Canhão virado para a esquerda e para baixo
    - "2" - Canhão virado para a direita e para baixo
    - "3" - Canhão virado para a direita e para cima
    - "4" - Canhão virado para a esquerda e para cima
- O objetivo do jogo é posicionar os canhões nas torres de forma que todos os atacantes sejam atingidos por pelo menos uma bala e que nenhuma torre seja atingida por nenhuma bala. Se houver mais de uma solução possível, o jogo pode retornar qualquer uma delas. Por exemplo, para a entrada acima, uma possível saída seria:

```txt
.n..4..n.
.2..n....
.n..#..n.
....n..4.
.n..3..n.
```
