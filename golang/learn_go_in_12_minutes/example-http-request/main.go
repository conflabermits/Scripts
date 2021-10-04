package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "reflect"
)

func main() {
    fmt.Println("Hello World!")
    response := http_req("https://jsonplaceholder.typicode.com/posts/1")
//    response := http_req("https://jsonplaceholder.typicode.notadomain.yyz/posts/1")
    fmt.Println("\t", "response", reflect.TypeOf(response))
    fmt.Println(response)
}

func http_req(url string) string {
    resp, err := http.Get(url)
    fmt.Println("\t", "resp", reflect.TypeOf(resp))
    fmt.Println("\t", "err", reflect.TypeOf(err))
    if err != nil {
        return err.Error()
    } else {
        body, err := ioutil.ReadAll(resp.Body)
        fmt.Println("\t", "body", reflect.TypeOf(body))
        fmt.Println("\t", "err", reflect.TypeOf(err))
        if err != nil {
            return err.Error()
        } else {
            return string(body)
        }
    }
}

