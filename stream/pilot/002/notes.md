# Summary

This is very much a "I'm trying to make programming Thing A easier by creating Thing B" situation.

# Problem Statement

I'm working on a small, simple program for work that we can use to check the health of the web applications we manage. Technically we already have a program that does this, but I'm rewriting the current tool as an opportunity learn Go-lang in addition to improving on the original product.

One of the challenges in writing a program that makes an HTTP request to a remote endpoint is that you can't always control that endpoints or rely on its response. That's the purpose of writing the program, but also what makes it hard to test and verify its reliability.

# Proposed Solution

What I'm planning to build is a simple web server that serves reliable, expected, static results. When I hit a specific endpoint I should know what the expected result is, and should get back the same result every time. Also, I should be able to get back responses that may be difficult to reliably replicate on uncontrolled sites, like 404, 302, and 501 responses.

## Requests and Expected Responses

| Request | HTTP Response Code | Response Content |
| --- | --- | --- |
| http://localhost:8080/ok | 200 | Health check response: "OK" |
| http://localhost:8080/degraded | 200 | Health check response: "Degraded" |
| http://localhost:8080/outage | 200 | Health check response: "Outage" |
| http://localhost:8080/200 | 200 | Blank page |
| http://localhost:8080/301 | 301 | Redirect to /200 |
| http://localhost:8080/302 | 302 | Redirect to /200 |
| http://localhost:8080/401 | 401 | Message indicating not authorized |
| http://localhost:8080/404 | 404 | Page not found |
| http://localhost:8080/501 | 501 | Server error |


# Helpful Resources

To be determined...