# Trusty Web Server

This is a simple web server with a simple goal: to respond with a consistent set of responses (HTTP response code, content, and/or actions) based on the endpoint requested.

It can be used for testing programs that make requests to a web server. The value is that the responses are consistent and predictable, which allows you to validate the functionality of the program making the requests instead of second-guessing if the remote endpoint is responding reliably.

## Requests and Expected Responses

| Request | HTTP Response Code | Response Content | Action |
| --- | --- | --- | --- |
| http://localhost:8080/ok | 200 | Health check response: "OK" |  |
| http://localhost:8080/degraded | 200 | Health check response: "Degraded" |  |
| http://localhost:8080/outage | 200 | Health check response: "Outage" |  |
| http://localhost:8080/200 | 200 | (Blank page) |  |
| http://localhost:8080/301 | 301 | | Redirect to "/200" |
| http://localhost:8080/302 | 302 | | Redirect to "/ok" |
| http://localhost:8080/401 | 401 | "Not authorized" |  |
| http://localhost:8080/404 | 404 | "Page not found" |  |
| http://localhost:8080/500 | 500 | "Internal server error" |  |
| http://localhost:8080/headers | 200 | Client headers |  |

## Running the server

The web server can be run as-is using `go run`:
```
$ go run trusty_web_server.go
```

It can also be compiled into a binary for easier portability:
```
$ go build trusty_web_server.go
```

In either case it will run on port 8080 by default.

It takes `--port` as an optional argument, allowing you to specify which port the web server should be served on:
```
go run trusty_web_server.go --port 38080
```

# Resources and References

* [Stream Notes](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/002/notes.md)
* [Example HTTP server code](https://gobyexample.com/http-servers)
* [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [How to set HTTP status code in response in Go](https://golangbyexample.com/set-http-status-code-golang/)
* [Example of setting HTTP redirect in Golang](https://gist.github.com/hSATAC/5343225)
