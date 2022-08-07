package main

import (
	"fmt"
	"os"
)

func main() {
	content, err := os.ReadFile("appname-OK.json")
	if err != nil {
		os.Exit(7)
	}
	fmt.Println(string(content))
}
