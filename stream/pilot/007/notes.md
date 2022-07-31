# Pilot Stream 007 Notes

The same but different.

## Summary

I'm looking to do something a little different with this stream, but using some existing work. My goal is to migrate one of my projects, the [Trusty Web Server](https://github.com/conflabermits/Scripts/tree/main/golang/trusty_web_server), from the `golang` directory in my general purpose `Scripts` repo to its own brand new repo, and in the process to also learn more about how to structure a Go project for optimal sharing, packaging, and versioning.

In other words:

* I want Trusty Web Server in its own GitHub repository
* I want the code broken out into a directory structure that makes it easier to test, package, and import
* I want to try cutting a versioned release of the project from GitHub
* If I have time, I'd also like to make some enhancements to the program and code:
  * Break out the static JSON responses into separate files
  * Make the response functions more general-purpose so I have fewer functions covering more responses
  * Add unit tests

## References

* [How do I Structure my Go Project?](https://www.wolfe.id.au/2020/03/10/how-do-i-structure-my-go-project/), from [Mark Wolfe's Blog](https://www.wolfe.id.au/)
* [Go - Project Structure and Guidelines](https://dev.to/jinxankit/go-project-structure-and-guidelines-4ccm), from [Ankit Kumar](https://dev.to/jinxankit) on [DEV Community](https://dev.to/)
