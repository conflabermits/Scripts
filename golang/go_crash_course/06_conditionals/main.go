package main

import "fmt"

func main() {
  x, y := 10, 10

  if x < y {
    fmt.Printf("%d is less than %d\n", x, y)
  }
  if x > y {
    fmt.Printf("%d is greater than %d\n", x, y)
  }
  if x <= y {
    fmt.Printf("%d is less than or equal to %d\n", x, y)
  } else {
    fmt.Printf("%d is NOT less than or equal to %d\n", x, y)
  }

  // else if
  color := "green"

  if color == "red" {
    fmt.Println("Color is red!")
  } else if color == "blue" {
    fmt.Println("Color is blue!")
  } else {
    fmt.Println("Color is neither red nor blue")
  }
}

