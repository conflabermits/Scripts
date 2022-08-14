# Spotify API Tester

More to come...

## Usage

So far I've only documented `search.go`.

### search.go

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

## References

Some examples pulled from [here](https://github.com/zmb3/spotify/blob/master/examples/], and *usually* modified as part of my learning process.

