package main

/*
Desafio:
1. Cria um baralho de N cartas;
2. A carta do topo é removida e separada do baralho;
3. A próxima carta é movida para a base do baralho;
4. Repete até que sobre uma carta;

INPUT: número de cartas (int);
OUTPUT: array com cartas removidas na sequência
    e última carta que restou ([]int,int);
*/

import (
	"encoding/json"
	"fmt"
	// "log"
	"os"
	"strconv"
)

// type resp struct {
// 	A []int
// 	B int
// }

func main() {
	// fmt.Println(Embaralha2(recive_int()))

	a, b := Embaralha2(recive_int())
	// fmt.Println(a, b)

	// // v := resp{
	// // 	a,
	// // 	b,
	// // }
	// v := [][]int{a, []int{b}}
	// fmt.Println(v)
	// res, _ := json.Marshal(v)
	// fmt.Println(string(res))

	// print("[")
	// res, _ := json.Marshal(a)
	// print(string(res))
	// print(",")
	// res, _ = json.Marshal(b)
	// print(string(res))
	// println("]")

  
  print_res(a,b)
}

func recive_int() int {
	// args := os.Args
	// if len(args) != 2 {
	// 	log.Fatal("Need to recieve just one number as argumment!")
	// }
	// n, err := strconv.Atoi(args[1])
	// if err != nil {
	// 	log.Println("Need to recieve a number as argumment!")
	// 	log.Fatal(err)
	// }
	n, _ := strconv.Atoi(os.Args[1])
	return n
}

func print_res(a []int, b int) {
  fmt.Print("[")
	res, _ := json.Marshal(a)
	fmt.Print(string(res))
	fmt.Print(",")
	res, _ = json.Marshal(b)
	fmt.Print(string(res))
	fmt.Println("]")

  //fmt.Print("[[")
  //l:=len(a)
  //for i,v := range a{
  //  fmt.Print(v)
  //  if i<l-1{
  //    fmt.Print(",")
  //  }
  //}
  //fmt.Print("],")
  //fmt.Print(b)
  //fmt.Println("]")
}
