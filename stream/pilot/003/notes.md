# Summary

I'm trying to take an existing [health check](https://github.com/conflabermits/Scripts/tree/master/golang/health_checker) tool written in Go/golang and add a few features to it. I don't know Go.

(This is a follow-up from [the previous stream](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/002/notes.md) where I built a simple web server.)

# Details

I'm working on a small, simple program for work that we can use to check the health of the web applications we manage. Technically we already have a program that does this, but I'm rewriting the current tool as an opportunity learn Go in addition to improving on the original product.

The tool is currently capable of making an HTTP request to an endpoint, collecting the JSON, parsing it, and pretty-printing the output.

## Updates to `health_checker`

There are a few features I want to add, at least one I want to remove, and other improvements I want to make. At a high level, I'm looking to:

* Remove the features around taking in a JSON file and focus on just the CLI and webserver modes.
* Integrate the webserver into the main binary, including the index page's HTML content, so it can be called from or run anywhere.
* Test and tweak the host header and timeout argument features.
* Test and tweak the user-agent request header.
* Optionally allow for the response to include HTTP response info.

## Updates to `trusty_web_server`

One of the challenges in writing a program that makes an HTTP request to a remote endpoint is that you can't always control that endpoints or rely on its response. That's the purpose of the [Trusty Web Server](https://github.com/conflabermits/Scripts/tree/master/golang/trusty_web_server) I built! It makes it easier to test and verify the reliability of the `health_checker` tool since the responses should always be static and consistent.

The web server needs some additional functionality to have it serve back the JSON responses we're expecting. I'll need to modify that tool to respond with JSON that matches the types of responses I'm expecting to check with the health_checker tool in addition to tweaking `health_checker` itself.

# Resources

* [Trusty Web Server](https://github.com/conflabermits/Scripts/tree/master/golang/trusty_web_server)
* [Health Checker](https://github.com/conflabermits/Scripts/tree/master/golang/health_checker)
* [Stream Notes](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/003/notes.md)
* [Google](https://google.com), probably
