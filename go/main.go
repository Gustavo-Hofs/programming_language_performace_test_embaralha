package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strconv"
)

func main() {
	a, b := Embaralha2(recive_int())
  print_res(a,b)
}

func recive_int() int {
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
}
