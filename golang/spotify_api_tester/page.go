package main

import (
	"context"
	"log"
	"os"
	"reflect"

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

	// Public playlist owned by noah.stride:
	// "Long playlist for testing pagination"
	//playlistID := "1ckDytqUi4BUYzs6HIhcAN"
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
	//log.Printf("Object 'tracks' is of type %v", reflect.TypeOf(tracks))
	//log.Printf("Object 'tracks.Items' is of type %v", reflect.TypeOf(tracks.Items))

	log.Printf("Playlist has %d total tracks", tracks.Total)
	for page := 1; ; page++ {
		log.Printf("  Page %d has %d tracks", page, len(tracks.Items))
		//log.Printf("Object 'tracks.Items' is of type %v", reflect.TypeOf(tracks.Items))
		log.Printf("Object 'tracks.Items[17].Track.Track.Name' is of type %v", reflect.TypeOf(tracks.Items[17].Track.Track.Name))
		log.Printf("Object 'tracks.Items[17].Track.Track.Name' == %v", tracks.Items[17].Track.Track.Name)
		log.Printf("Object 'tracks.Items[17].Track.Track.SimpleTrack.Artists[0].Name' is of type %v", tracks.Items[17].Track.Track.SimpleTrack.Artists[0].Name)
		log.Printf("Object 'tracks.Items[17].Track.Track.SimpleTrack.Artists[0].Name' == %v", tracks.Items[17].Track.Track.SimpleTrack.Artists[0].Name)
		err = client.NextPage(ctx, tracks)
		if err == spotify.ErrNoMorePages {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
	}

	/*
		playlistTrack, err := client.GetPlaylistTracksOpt(
			ctx,
			spotify.ID(playlistID),
			fields = "items(track(name,href,album(name,href)))"
		)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("Playlist %d tracks:", playlistTrack.name)
	*/
}
