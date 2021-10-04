package main

import (
    "fmt"
    "io/ioutil"
    "encoding/json"
    "os"
    "reflect"
)

func parse_json_file(input_file string) map[string]interface {} {

    jsonFile, err := os.Open(input_file)
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println("Successfully opened json file")
    }
    defer jsonFile.Close()
    fmt.Println("\t", "jsonFile", reflect.TypeOf(jsonFile))

    byteValue, _ := ioutil.ReadAll(jsonFile)
    fmt.Println("\t", "byteValue", reflect.TypeOf(byteValue))

    var result map[string]interface{}
    fmt.Println("\t", "result", reflect.TypeOf(result))

    json.Unmarshal([]byte(byteValue), &result)
    fmt.Println("\t", "&result", reflect.TypeOf(&result))

    return result

}

func main() {

    fmt.Println("Hello World!")

    json := parse_json_file("app1.json")
    fmt.Println("\t", "json", reflect.TypeOf(json))
    fmt.Println(json["name"], json["statusCode"])

}

