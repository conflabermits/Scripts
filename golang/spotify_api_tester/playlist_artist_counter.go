package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"
	"sort"

	"github.com/zmb3/spotify/v2"
	spotifyauth "github.com/zmb3/spotify/v2/auth"
	"golang.org/x/oauth2/clientcredentials"
)

type Options struct {
	PlaylistID string
	MinCount   int
	MaxResults int
}

func parseArgs() (*Options, error) {
	options := &Options{}

	flag.StringVar(&options.PlaylistID, "playlist", "", "Playlist to check")
	flag.IntVar(&options.MinCount, "count", 2, "Minimum result count per artist")
	flag.IntVar(&options.MaxResults, "max", 20, "Maximum results returned")
	flag.Usage = func() {
		fmt.Printf("Usage: <program> -playlist <playlist> [options]\n\n")
		flag.PrintDefaults()
	}
	flag.Parse()

	return options, nil
}

func main() {
	options, err := parseArgs()

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

	playlistID := options.PlaylistID //"4APcFEwscoVfmwJelij53o"

	tracks, err := client.GetPlaylistItems(
		ctx,
		spotify.ID(playlistID),
	)
	if err != nil {
		log.Fatal(err)
	}

	artistmap := make(map[string]int)
	//log.Printf("Playlist has %d total tracks", tracks.Total)

	for page := 1; ; page++ {
		//log.Printf("  Page %d has %d tracks", page, len(tracks.Items))
		for _, track := range tracks.Items {
			for _, artist := range track.Track.Track.SimpleTrack.Artists {
				artistname := string(artist.Name)
				artistmap[artistname]++
			}
		}
		err = client.NextPage(ctx, tracks)
		if err == spotify.ErrNoMorePages {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
	}
	//log.Printf("raw artistmap:\n%v", artistmap)

	keys := make([]string, 0, len(artistmap))
	for key := range artistmap {
		keys = append(keys, key)
	}
	//log.Printf("unsorted keys:\n%v", keys)

	sort.SliceStable(keys, func(i, j int) bool {
		return artistmap[keys[i]] > artistmap[keys[j]]
	})
	//log.Printf("sorted keys:\n%v", keys)

	for i, key := range keys {
		if (artistmap[key] >= options.MinCount) && (i < options.MaxResults) {
			progress := ""
			for i := 1; i < artistmap[key]; i++ {
				progress += "▓"
			}
			fmt.Printf("%s %d %s\n", progress, artistmap[key], key) //credit: @TheD3vil
			//fmt.Printf("%d || %s\n", artistmap[key], key)
		} else {
			break
		}
	}

}
