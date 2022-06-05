# Trusty Web Server

Create a web server that can be used for testing programs that make calls to a web server. The goal is to make responses consistent and predictable to ensure the program making the requests is working properly.

## Requests and Expected Responses

| Request | HTTP Response Code | Response Content | Status |
| --- | --- | --- | --- |
| http://localhost:8080/ok | 200 | Health check response: "OK" | DONE |
| http://localhost:8080/degraded | 200 | Health check response: "Degraded" | DONE |
| http://localhost:8080/outage | 200 | Health check response: "Outage" | DONE |
| http://localhost:8080/200 | 200 | Blank page | DONE |
| http://localhost:8080/301 | 301 | Redirect to /200 | DONE |
| http://localhost:8080/302 | 302 | Redirect to /ok | DONE |
| http://localhost:8080/401 | 401 | Message indicating not authorized | DONE |
| http://localhost:8080/404 | 404 | Page not found | DONE |
| http://localhost:8080/500 | 500 | Internal server error | DONE |

# Resources and References

* [Stream Notes](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/002/notes.md)
* [Example HTTP server code](https://gobyexample.com/http-servers)
* [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [How to set HTTP status code in response in Go](https://golangbyexample.com/set-http-status-code-golang/)
* [Example of setting HTTP redirect in Golang](https://gist.github.com/hSATAC/5343225)
