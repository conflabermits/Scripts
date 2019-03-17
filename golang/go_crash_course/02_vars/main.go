package main

import "fmt"

func main() {
  // MAIN TYPES
  // string
  // bool
  // int
  // int  int8  int16  int32  int64
  // uint uint8 uint16 uint32 uint64 uintptr
  // byte - alias for uint8
  // rune - alias for int32
  // float32 float64
  // complex64 complex128

  // Using var
  var name string = "Chris"
  // Also works: var name = "Chris"
  // var type is inferred in some cases based on the value assigned to it

  // vars also need to be used in the program. unsused vars raise errors at runtime
  // For example: 02_vars/main.go:23:7: age declared and not used
  var age = 74

  // Shorthand for variable declaration (inside main)
  // name := "Chris"
  height, email := 5.5, "chris@email.liame"

  var isCool = false
  isCool = true
  // if i use const instead of var, i wouldn't be able to change it from false to true

  // fmt.Println(name, age, isCool)
  fmt.Printf("%v\t%v\t%v\t%v\t%v\n", name, age, height, isCool, email)

  // fmt lets us grab the type of a var using %T
  // fmt.Printf("%T\n", name)
  // fmt.Printf("%T\n", age)

  // or, you know, print both on the same line ;-)
  fmt.Printf("%T\t%T\t%T\t%T\t%T\n", name, age, height, isCool, email)


}

