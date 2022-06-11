# What Do We Want It To Do?

At a minimum we want golang binaries that can perform health checks against endpoints that respond with JSON.

Ideally we want to improve upon this minimum design in several ways:

* Allow for several CLI options with sane default values that make the script more flexible
  * Host header
  * Timeout
* Ensure JSON output is "pretty"
* Allow for output to include HTTP response information
* Parse the response into "short", "full", and "dynamic" lengths using an optional CLI argument
* Include testing (potentially using trusty_web_server)
* Include a webserver binary that pulls in the main binary and performs testing using a simple web form/UI
  * Page allows users to specify most or all of the same options as the CLI
  * Page returns "pretty" response JSON and info
  * Page allows for users to submit another URL when returning the response of a previous request


# Extra Credit

Most of these are just nice-to-have and not requirements. The list is roughly sorted into a priority order.

* Either combine the two binaries into one, or link them to a common function library to prevent logic duplication
* Add a conditional statement so an empty "broken_components" array isn't returned in Dynamic depth
* Allow the web binary to be run from any path
    * Probably need to include the HTML template directly in the code for web.go so it's packaged into the binary
* Remove all those extra comments of code that was used to test and debug and verify functionality
* Toss it in a docker scratch container
* Make the HTML pretty
* Tweak the user-agent values to something custom and potentially include date string
* Allow users to supply additional headers via args
* Build tests using sample JSON and HTTP response failure text
* Remove the JSON file logic

