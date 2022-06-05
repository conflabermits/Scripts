# Summary

This is very much a "I'm trying to make programming Thing A easier by creating Thing B" situation.

# Problem Statement

I'm working on a small, simple program for work that we can use to check the health of the web applications we manage. Technically we already have a program that does this, but I'm rewriting the current tool as an opportunity learn Go-lang in addition to improving on the original product.

One of the challenges in writing a program that makes an HTTP request to a remote endpoint is that you can't always control that endpoints or rely on its response. That's the purpose of writing the program, but also what makes it hard to test and verify its reliability.

# Proposed Solution

What I'm planning to build is a simple web server that serves reliable, expected, static results. When I hit a specific endpoint I should know what the expected result is, and should get back the same result every time. Also, I should be able to get back responses that may be difficult to reliably replicate on uncontrolled sites, like 404, 302, and 501 responses.

## Requests and Expected Responses

| Request | HTTP Response Code | Response Content | Status |
| --- | --- | --- | --- |
| http://localhost:8080/ok | 200 | Health check response: "OK" | DONE |
| http://localhost:8080/degraded | 200 | Health check response: "Degraded" | DONE |
| http://localhost:8080/outage | 200 | Health check response: "Outage" | DONE |
| http://localhost:8080/200 | 200 | Blank page | DONE |
| http://localhost:8080/301 | 301 | Redirect to /200 | DONE |
| http://localhost:8080/302 | 302 | Redirect to /200 | DONE |
| http://localhost:8080/401 | 401 | Message indicating not authorized | DONE |
| http://localhost:8080/404 | 404 | Page not found | DONE |
| http://localhost:8080/500 | 500 | Internal server error | DONE |


# Helpful Resources

* [Go by Example: HTTP Servers](https://gobyexample.com/http-servers)
* [Sample web server code (to borrow from)](https://github.com/conflabermits/Scripts/blob/master/golang/trusty_web_server/sample.go)