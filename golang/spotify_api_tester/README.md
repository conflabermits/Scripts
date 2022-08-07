# Spotify API Tester

More to come...

## Usage

Doesn't run if you don't specify a query

```text
$ go run main.go
Try specifying a word or phrase to search for

exit status 2
```

Help returns help text

```text
$ go run main.go -help
Usage: go run main.go -query "search string" [-type "album"]

  -query string
        Search string used to query Spotify API
  -type string
        Limit search to album, artist, track, or playlist only (default: track)
```

Search tracks for a query

```text
$ go run main.go -query "l'via l'viaquez" -type track
Searching tracks for l'via l'viaquez:
Track:
    L'Via L'Viaquez
    L'Via L'Viaquez - Radio Edit
```

Search artists for a query

```text
$ go run main.go -query "l'via l'viaquez" -type artist
Searching artists for l'via l'viaquez:
Artists:
```

Search albums for a query

```text
$ go run main.go -query "l'via l'viaquez" -type album
Searching albums for l'via l'viaquez:
Albums:
    L'Via L'Viaquez
```

Search playlists for a query

```text
$ go run main.go -query "l'via l'viaquez" -type playlist
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
$ go run main.go -query "l'via l'viaquez"
Searching tracks for l'via l'viaquez:
Track:
    L'Via L'Viaquez
    L'Via L'Viaquez - Radio Edit
```
