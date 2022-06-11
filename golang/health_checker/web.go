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
		response := health_checker_http_req(reqURL)
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

func health_checker_http_req(url string) string {
	client := &http.Client{
		Timeout: time.Second * 30,
	}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return err.Error()
	} else {
		req.Header.Set("user-agent", "health_checker-go-web")
		//req.Header.Add("X-Forwarded-Proto", "https")
		resp, err := client.Do(req)
		if err != nil {
			return err.Error()
		} else {
			body, err := ioutil.ReadAll(resp.Body)
			defer resp.Body.Close()
			if err != nil {
				return err.Error()
			} else {
				return string(body)
			}
		}
	}
}
