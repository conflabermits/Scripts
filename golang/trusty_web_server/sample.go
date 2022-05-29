package main

import (
	"flag"
	"fmt"
	"html/template"
	"io/ioutil"
	"net/http"
	"time"
)

type ResultDetails struct {
	Success  bool
	URL      string
	Depth    string
	Response string
}

func main() {

	port := flag.String("port", "8080", "Port to run the local web server")
	flag.Parse()

	tmpl := template.Must(template.ParseFiles("index.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			tmpl.Execute(w, nil)
			return
		}

		reqURL := r.FormValue("url")
		fmt.Println("Request URL: " + reqURL)
		reqDepth := r.FormValue("depth")
		fmt.Println("Request Depth: " + reqDepth)
		response := http_req(reqURL)
		//fmt.Println("Response: " + response)

		result := ResultDetails{
			Success:  true,
			URL:      reqURL,
			Depth:    reqDepth,
			Response: response,
		}
		tmpl.Execute(w, result)
	})

	http.ListenAndServe(":"+*port, nil)
}

