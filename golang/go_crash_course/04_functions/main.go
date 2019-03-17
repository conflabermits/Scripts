package main

import "fmt"

// format is func, name of function, input variables and types in parentheses, return value, then curly brackets
func greeting(name string) string {
  return "Hello " + name
}

// We can comma separate the input var declarations if they're the same type
func getSum(num1, num2 int) int {
  return num1 + num2
}

func main() {
  fmt.Println(greeting("Chris"))
  fmt.Println(getSum(3, 4))
}

