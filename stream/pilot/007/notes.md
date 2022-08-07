# Pilot Stream 007 Notes

The same but different.

## Summary

I'm looking to do something a little different with this stream, but using some existing work. My goal is to migrate one of my projects, the [Trusty Web Server](https://github.com/conflabermits/Scripts/tree/main/golang/trusty_web_server), from the `golang` directory in my general purpose `Scripts` repo to its own brand new repo, and in the process to also learn more about how to structure a Go project for optimal sharing, packaging, and versioning.

In other words:

* I want Trusty Web Server in its own GitHub repository ([Done!](https://github.com/conflabermits/trusty_web_server) ✅)
* I want the code broken out into a directory structure that makes it easier to test, package, and import ([Done!](https://github.com/conflabermits/trusty_web_server/commits/main) ✅)
* I want to try cutting a versioned release of the project from GitHub ([Done!](https://github.com/conflabermits/trusty_web_server/releases/tag/v0.1.0-alpha) ✅)
* If I have time, I'd also like to make some enhancements to the program and code:
  * Break out the static JSON responses into separate files
  * Make the response functions more general-purpose so I have fewer functions covering more responses
  * Add unit tests

## References

I've listed the pages I referred to both before and during the stream.

* [How do I Structure my Go Project?](https://www.wolfe.id.au/2020/03/10/how-do-i-structure-my-go-project/), from [Mark Wolfe's Blog](https://www.wolfe.id.au/)
* [Go - Project Structure and Guidelines](https://dev.to/jinxankit/go-project-structure-and-guidelines-4ccm), from [Ankit Kumar](https://dev.to/jinxankit) on [DEV Community](https://dev.to/)
* [Standard Go Project Layout](https://github.com/golang-standards/project-layout)
* [Go Documentation](https://go.dev/doc/)
  * [Tutorial: Get started with Go](https://go.dev/doc/tutorial/getting-started)
  * [Tutorial: Create a Go module](https://go.dev/doc/tutorial/create-module)
  * [Tutorial: Getting started with multi-module workspaces](https://go.dev/doc/tutorial/workspaces)
  * [How to Write Go Code](https://go.dev/doc/code)
