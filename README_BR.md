# programming_language_performace_test_embaralha
Performance comparison of programming languages.

### Objetivo
O objetivo desse projeto é comparar a performace das seguintes linguagens de programação:
- Python
- Go
- Rust
- Bash
- C++

### Metodo
Todas as linguagens devem implementar uma função que:

1. Cria um baralho de N cartas;
2. A carta do topo é removida e separada do baralho;
3. A próxima carta é movida para a base do baralho;
4. Repete até que sobre uma carta;
5. INPUT: número de cartas (int);
6. OUTPUT: array com cartas removidas na sequência
    e última carta que restou ([]int,int);

Para fazer o benchmark, foi utilizado pyperf.

### Execução
Pre requisitos:
- python
- pyperf
- go
- rust
- bash
- gpp
Para iniciar o benchmark, mostrar os resultados e deletar arquivos extras gerados:
~~~
./benchmar_baralhos.py
~~~
ou
~~~
./benchmar_baralhos.sh
~~~

### Resultados
![image](https://github.com/Gustavo-Hofs/programming_language_performace_test_embaralha/assets/54177943/0b5de0f3-ed91-4eff-a96a-0da7ba0953ae)

### Conclusão
