package main

import (
	"flag"
	"fmt"
	"net/http"
)

func respond_ok(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "OK\n")
}

func respond_degraded(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "Degraded\n")
}

func respond_outage(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "Outage\n")
}

func respond_200(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "\n")
}

func respond_401(w http.ResponseWriter, req *http.Request) {

    w.WriteHeader(401)
    fmt.Fprintf(w, "Not authorized\n")
}

func respond_404(w http.ResponseWriter, req *http.Request) {

    w.WriteHeader(404)
    fmt.Fprintf(w, "Page not found\n")
}

func respond_500(w http.ResponseWriter, req *http.Request) {

    w.WriteHeader(500)
    fmt.Fprintf(w, "Internal server error\n")
}

func respond_301(w http.ResponseWriter, req *http.Request) {

    http.Redirect(w, req, "/200", 301)

}

func respond_302(w http.ResponseWriter, req *http.Request) {

    http.Redirect(w, req, "/ok", 302)

}

func headers(w http.ResponseWriter, req *http.Request) {

    for name, headers := range req.Header {
        for _, h := range headers {
            fmt.Fprintf(w, "%v: %v\n", name, h)
        }
    }
}

func main() {

	port := flag.String("port", "8080", "Port to run the local web server")
	flag.Parse()

    http.HandleFunc("/ok", respond_ok)
    http.HandleFunc("/degraded", respond_degraded)
    http.HandleFunc("/outage", respond_outage)

    http.HandleFunc("/200", respond_200)
    http.HandleFunc("/301", respond_301)
    http.HandleFunc("/302", respond_302)
    http.HandleFunc("/401", respond_401)
    http.HandleFunc("/404", respond_404)
    http.HandleFunc("/500", respond_500)

    http.HandleFunc("/headers", headers)

    http.ListenAndServe(":"+*port, nil)
}
