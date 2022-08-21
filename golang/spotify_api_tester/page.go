package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"sort"

	"github.com/zmb3/spotify/v2"
	spotifyauth "github.com/zmb3/spotify/v2/auth"
	"golang.org/x/oauth2/clientcredentials"
)

func main() {
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

	playlistID := "4APcFEwscoVfmwJelij53o"
	if id := os.Getenv("SPOTIFY_PLAYLIST"); id != "" {
		playlistID = id
	}

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
	for _, key := range keys {
		if artistmap[key] > 2 {
			fmt.Printf("%d || %s\n", artistmap[key], key)
		}
	}
}
