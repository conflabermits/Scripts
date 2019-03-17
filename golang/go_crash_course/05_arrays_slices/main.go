package main

import "fmt"

func main() {
  // Arrays
  var fruitArr [2] string
  // above declares the array as a 2-element array
  // you can't add a third value to the array
  // you can declar the size and type with or without a space between

  // Assign values
  fruitArr[0] = "Apple"
  fruitArr[1] = "Orange"

  // Declare AND assign example
  fruitArr2 := [2]string{"Banana", "Pear"}

  fruitSlice := []string{"Grape", "Lime", "Lemon"}

  fmt.Println(fruitArr)
  fmt.Println(fruitArr[1])
  fmt.Println(fruitArr2)
  fmt.Println(fruitSlice)
  fmt.Println(len(fruitSlice))
  //range print starts at first value and stop before second
  fmt.Println(fruitSlice[1:2])
  fmt.Println(fruitSlice[1:3])
}

