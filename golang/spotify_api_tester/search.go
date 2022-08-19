package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"

	spotifyauth "github.com/zmb3/spotify/v2/auth"

	"golang.org/x/oauth2/clientcredentials"

	"github.com/zmb3/spotify/v2"
)

type Options struct {
	Query string
	Type  string
}

func parseArgs() (*Options, error) {
	options := &Options{}

	flag.StringVar(&options.Query, "query", "", "Search string used to query Spotify API")
	flag.StringVar(&options.Type, "type", "", "Limit search to album, artist, track, or playlist only (default: track)")
	flag.Usage = func() {
		fmt.Printf("Usage: go run main.go -query \"search string\" [-type \"album\"]\n\n")
		flag.PrintDefaults()
	}
	flag.Parse()

	return options, nil
}

func search() {
	options, err := parseArgs()
	if err != nil {
		os.Exit(1)
	}

	if options.Query == "" {
		fmt.Print("Try specifying a word or phrase to search for\n\n")
		os.Exit(2)
	}

	if options.Type == "" {
		options.Type = "track"
	}

	ctx := context.Background()
	config := &clientcredentials.Config{
		ClientID:     os.Getenv("SPOTIFY_ID"),
		ClientSecret: os.Getenv("SPOTIFY_SECRET"),
		TokenURL:     spotifyauth.TokenURL,
	}
	token, err := config.Token(ctx)
	if err != nil {
		log.Fatalf("couldn't get token: %v", err)
	}

	httpClient := spotifyauth.New().Client(ctx, token)
	client := spotify.New(httpClient)

	// conditionally search albums, artists, songs, or playlists
	switch options.Type {
	case "album", "albums":
		fmt.Print("Searching ", options.Type, "s for ", options.Query, ":\n")
		results, err := client.Search(ctx, options.Query, spotify.SearchTypeAlbum)
		if err != nil {
			log.Fatal(err)
		}
		if results.Albums != nil {
			fmt.Println("Albums:")
			for _, item := range results.Albums.Albums {
				fmt.Println("   ", item.Name)
			}
		}
	case "artist", "artists":
		fmt.Print("Searching ", options.Type, "s for ", options.Query, ":\n")
		results, err := client.Search(ctx, options.Query, spotify.SearchTypeArtist)
		if err != nil {
			log.Fatal(err)
		}
		if results.Artists != nil {
			fmt.Println("Artists:")
			for _, item := range results.Artists.Artists {
				fmt.Println("   ", item.Name)
			}
		}
	case "playlist", "playlists":
		fmt.Print("Searching ", options.Type, "s for ", options.Query, ":\n")
		results, err := client.Search(ctx, options.Query, spotify.SearchTypePlaylist)
		if err != nil {
			log.Fatal(err)
		}
		if results.Playlists != nil {
			fmt.Println("Playlists:")
			for _, item := range results.Playlists.Playlists {
				fmt.Println("   ", item.Name)
			}
		}
	case "track", "tracks":
		fmt.Print("Searching ", options.Type, "s for ", options.Query, ":\n")
		results, err := client.Search(ctx, options.Query, spotify.SearchTypeTrack)
		if err != nil {
			log.Fatal(err)
		}
		if results.Tracks != nil {
			fmt.Println("Track:")
			for _, item := range results.Tracks.Tracks {
				fmt.Println("   ", item.Name)
			}
		}
	}

}
