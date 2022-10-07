# Pilot Stream 013 Notes

## Summary

Wrapping up work on [trusty_web_server](https://github.com/conflabermits/trusty_web_server) to make it release-ready! It's so close!

## Details

In the last stream I fixed up [health_checker](https://github.com/conflabermits/health_checker). Now It's time to do the same for trusty_web_server.

This stream I'm looking to close a couple other gaps and prepare the application for a v1.0.0 release:

* Embed the json files into the binary properly for easier distribution as a single-file web server program.
* Restructure the project directories to put static files somewhere other than `pkg`.
* Test, update documentation, push, and cut a final release version of the program!
* Stretch goal: Add proper request/access logging to STDOUT.

## References

* [health_checker](https://github.com/conflabermits/health_checker) repo
* [trusty_web_server](https://github.com/conflabermits/trusty_web_server) repo
* [Twitch channel](https://twitch.tv/conflabermits)
