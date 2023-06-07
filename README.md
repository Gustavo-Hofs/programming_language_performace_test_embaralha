# Performance comparison Embaralha

### Goal
The objective of this project is to compare the performance of the following programming languages:
- Python
- Go
- Rust
- Bash
- C++

### Method
All languages must implement a function that:

1. Creates a deck of N cards;
2. The top card is removed and separated from the deck;
3. The next card is moved to the bottom of the deck;
4. Repeat until you have one card left;
5. INPUT: number of cards (int);
6. OUTPUT: array with cards removed in sequence and last card left ([]int,int);

To do the benchmark, pyperf was used.

### Execution
Prerequisites:
- python
- pyperf
- go
- rust
- bash
- gpp

To start the benchmark, display the results and delete generated extra files:
~~~
./benchmar_baralhos.py
~~~
or
~~~
./benchmar_baralhos.sh
~~~

### Results
![image](https://github.com/Gustavo-Hofs/programming_language_performace_test_embaralha/assets/54177943/0b5de0f3-ed91-4eff-a96a-0da7ba0953ae)

### Conclusion
In this benchmark, Bash performed surprisingly slowly, even slower than Python.
Python was slower and needed more memory than C++, Go, and Rust.
C++ was slower than Go and Rust.
Rust was faster and needed less memory than Go.
