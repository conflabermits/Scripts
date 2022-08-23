# Spotify API Tester

So far we've got TWO programs: `search.go` and `playlist_artist_counter.go`.

Both programs require Spotify API credentials. To run these programs from the command line, it's necessary to load `SPOTIFY_ID` and `SPOTIFY_SECRET` into environment variables.

## search.go

`search.go` is a program that will search Spotify for albums, artists, tracks, or playlists matching a string.

### Examples

Doesn't run if you don't specify a query

```text
$ go run search.go
Try specifying a word or phrase to search for

exit status 2
```

Help returns help text

```text
$ go run search.go -help
Usage: go run search.go -query "search string" [-type "album"]

  -query string
        Search string used to query Spotify API
  -type string
        Limit search to album, artist, track, or playlist only (default: track)
```

Search tracks for a query

```text
$ go run search.go -query "l'via l'viaquez" -type track
Searching tracks for l'via l'viaquez:
Track:
    L'Via L'Viaquez
    L'Via L'Viaquez - Radio Edit
```

Search artists for a query

```text
$ go run search.go -query "l'via l'viaquez" -type artist
Searching artists for l'via l'viaquez:
Artists:
```

Search albums for a query

```text
$ go run search.go -query "l'via l'viaquez" -type album
Searching albums for l'via l'viaquez:
Albums:
    L'Via L'Viaquez
```

Search playlists for a query

```text
$ go run search.go -query "l'via l'viaquez" -type playlist
Searching playlists for l'via l'viaquez:
Playlists:
    L'Via L'Viaquez
    L'Via L'Viaquez
    L'Via L'Viaquez
    L'Via L'Viaquez
    L'Via L'Viaquez
    L'Via L'Viaquez
```

Only specifying query will default to search type "track"

```text
$ go run search.go -query "l'via l'viaquez"
Searching tracks for l'via l'viaquez:
Track:
    L'Via L'Viaquez
    L'Via L'Viaquez - Radio Edit
```

## playlist_artist_counter.go

`playlist_artist_counter.go` is a program that will count how many times each artist appears in a playlist and return the results in decending order.

Right now it shows the artists and the number of their appearances next to bars of length equal to the count of appearances. There are currently hard-coded values for the playlist ID, which can be replaced if an environment variable called `SPOTIFY_PLAYLIST` is present, and for the number of results it will display, currently set to artists with more than 2 appearances.

### Examples

Running with defaults

```text
$ go run playlist_artist_counter.go
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 17 System Of A Down
▓▓▓▓▓▓▓▓▓▓▓▓▓ 14 Red Hot Chili Peppers
▓▓▓▓▓▓▓▓▓▓▓▓ 13 The Offspring
▓▓▓▓▓▓▓▓▓▓▓ 12 Foo Fighters
▓▓▓▓▓▓▓▓▓▓ 11 Green Day
▓▓▓▓▓▓▓▓▓▓ 11 Rage Against The Machine
▓▓▓▓▓▓▓▓▓▓ 11 Linkin Park
▓▓▓▓▓▓▓▓▓ 10 Nirvana
▓▓▓▓▓▓▓▓ 9 blink-182
▓▓▓▓ 5 The White Stripes
▓▓▓ 4 Muse
▓▓▓ 4 Sublime
▓▓▓ 4 CAKE
▓▓ 3 Tame Impala
▓▓ 3 The Smashing Pumpkins
▓▓ 3 Method Man
▓▓ 3 Queens of the Stone Age
▓▓ 3 The Strokes
▓▓ 3 Missy Elliott
▓▓ 3 Wu-Tang Clan
▓▓ 3 311
```

Setting the SPOTIFY_PLAYLIST environment variable with a different playlist ID (containing far more songs)

```text
$ export SPOTIFY_PLAYLIST='5XlcCts6DcfojIU5jTAELu'
$ go run playlist_artist_counter.go
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 42 System Of A Down
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 41 Green Day
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 26 Foo Fighters
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 26 Red Hot Chili Peppers
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 26 Rage Against The Machine
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 23 blink-182
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 16 Linkin Park
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 16 The Offspring
▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 15 Nirvana
▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 15 Muse
▓▓▓▓▓▓▓▓▓▓▓▓ 13 Sublime
▓▓▓▓▓▓▓▓▓▓▓ 12 Pennywise
▓▓▓▓▓▓▓▓▓▓ 11 Arctic Monkeys
▓▓▓▓▓▓▓▓▓▓ 11 Minor Threat
▓▓▓▓▓▓▓▓▓▓ 11 Misfits
▓▓▓▓▓▓▓▓▓ 10 No Doubt
▓▓▓▓▓▓▓▓▓ 10 Beastie Boys
▓▓▓▓▓▓▓▓▓ 10 Queens of the Stone Age
    ...
    snip
    ...
```

## References

Some examples pulled from [here](https://github.com/zmb3/spotify/blob/master/examples/), and *usually* modified as part of my learning process.

Other links as I've recalled or recorded:

* [Hard-coded Spotify playlist](https://open.spotify.com/playlist/4APcFEwscoVfmwJelij53o)
* [Stream notes](https://github.com/conflabermits/Scripts/blob/main/stream/pilot/009/notes.md)
* [Spotify API: Get Playlist Items](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks)
* [Go By Example](https://gobyexample.com):
  * [Maps](https://gobyexample.com/maps)
  * [Range](https://gobyexample.com/range)
* [zmb3/spotify#SimpleTrack documentation](https://pkg.go.dev/github.com/zmb3/spotify#SimpleTrack)
* [GeeksForGeeks: How to Sort Golang Map By Keys or Values?](https://www.geeksforgeeks.org/how-to-sort-golang-map-by-keys-or-values)
