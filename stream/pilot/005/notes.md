# Summary

Goals for today's stream:

* Finish the python wordle helper
* Improve the stream

# Python Wordle Helper

I started building a wordle helper in python [here](https://github.com/conflabermits/Scripts/tree/main/python/wordle). I have some work remaining to finish it like implementing the logic for yellows and for duplicate latters.

# Improve The Stream

I noticed in a recording of the previous stream that the audio levels seemed really low, but I think I fixed that. I still want to figure out how to tweak the audio settings to allow background music to play while I stream but to prevent it from being saved in the stream recording or posted to Twitch. I also need to figure out how to either upload recorded videos to Twitch or to allow Twitch to save the stream recording.

# Future Streams

I'm still working out what else I'd want to do on stream. The goals above are good for the 005 stream but looking ahead at future streams I have a few ideas of what I want to work on or share, some more defined than others.

* Finish the golang [health_checker](https://github.com/conflabermits/Scripts/tree/main/golang/health_checker) I started about a month ago
    * Finish feature implementation
    * Incorporate web server element
    * Figure out if there's a better way to build it all without literally making it a single giant Go file
* Take a stab at creating a Wordle Helper in Go and building it into a standalone webapp thing
* Mess around with Docker (no clear ideas yet)
* Mess around with WSL templating or provisioning, maybe with the goal of establishing a ready-to-go DevOps/development platform that has a bunch of tools and programs preinstalled like Git, Terraform, kubectl, python3, golang, aws cli, etc.
* Learn and implement some Go testing best practices and add it to the [health_checker](https://github.com/conflabermits/Scripts/tree/main/golang/health_checker) program/project