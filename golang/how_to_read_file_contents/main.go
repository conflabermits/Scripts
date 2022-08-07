package main

import (
	"fmt"
	"os"
)

func loadText(file string) string {
	content, err := os.ReadFile(file)
	if err != nil {
		os.Exit(7)
	}
	return string(content)
}

func main() {
	fmt.Println("Start of program")
	filecontent := loadText("appname-OK.json")
	fmt.Println(filecontent)
	fmt.Println("End of program")
}
