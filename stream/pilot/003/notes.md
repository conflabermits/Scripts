# Summary

I'm trying to take an existing health check tool written in Go/golang and add a few features to it. I don't know Go.

(This is a follow-up from [the previous stream](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/002/notes.md) where I built a simple web server.)

# Problem Statement

I'm working on a small, simple program for work that we can use to check the health of the web applications we manage. Technically we already have a program that does this, but I'm rewriting the current tool as an opportunity learn Go in addition to improving on the original product.

The tool is currently capable of making an HTTP request to an endpoint, collecting the JSON, parsing it, and pretty-printing the output.

# Proposed Solution

There are a few features I want to add, at least one I want to remove, and other improvements I want to make. All are detailed in the readme for the [health_checker](https://github.com/conflabermits/Scripts/tree/master/golang/health_checker) project.

# Resources

## Trusty Web Server

One of the challenges in writing a program that makes an HTTP request to a remote endpoint is that you can't always control that endpoints or rely on its response. That's the purpose of the [trusty_web_server](https://github.com/conflabermits/Scripts/tree/master/golang/trusty_web_server) I built! It makes it easier to test and verify the reliability of the health_checker tool since the responses should always be static and consistent.

