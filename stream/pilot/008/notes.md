# Pilot Stream 008 Notes

"How much can I do with the Spotify API without knowing a lot of Go?"

## Summary

I don't know a lot of Go and I'm trying to learn more. In my experience, for me, the best way to learn is to have a goal in mind that challenges me to do something that I'd actually want to do. (Sorry "Hello World" examples, you just don't cut it anymore.)

In this stream I'm hoping to jump into using the Spotify API with very little preparation.

## Details

The only work I've done up to this point is:

* Ensuring I have a developer token for authentication and authorization with Spotify
* Putting the tokens in a file I can read into my environment
* Looking up a Go library that abstracts the nitty gritty bits of using Go to talk to Spotify and allows me to focus on the tasks I want to accomplish.

Until and unless this needs to be broken out into a separate repository, I'll keep the project in my Scripts repo [here](https://github.com/conflabermits/Scripts/tree/main/golang/spotify_api_tester).

## Goals

* Learn about the metadata associated with songs, artists, albums, and playlists
* Learn how to make a playlist and:
  * Add songs to it
  * Move songs within it
  * Remove songs from it

## References

* [Spotify Go library by zmb3 (GitHub)](https://github.com/zmb3/spotify)
* [zmb3's Go documentation for Spotify library](https://pkg.go.dev/github.com/zmb3/spotify)
* [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
