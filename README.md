# Iðunn

Convert exported Apple Music playlists to YAML.

## Why?

I love making playlists. Every year, every season, I make a playlist. That music becomes my soundtrack for that time in my life, and once it's gone, gives me a way for me to bring back a bygone moment.

I want a way to take snapshots of my playlists -- as text files, naturally, so they can be tracked in source control!

## How?

Apple Music provides a [way to export playlists](https://support.apple.com/guide/music/save-a-copy-of-your-playlists-mus27cd5060f/mac), either in TSV or XML.

![screenshot](docs/img/export-playlist.png)

These formats aren't human-readable. They do have an advantage in that you can use them to import the data back into Apple Music, so might want to keep them handy after you're done. Note the caveat, though:

> The imported playlist includes only songs and music videos already in your music library. Unavailable items are removed from the list.

Export as a text file (which is actually in TSV format). Then run:

```sh
idunn "My Playlist.txt"
```

This will produce a file named `My Playlist.yml`:

```yml
name: My Playlist
songs:
- name: Float On
  artist: Magic Mouse
  album: Good News for People Who Love Bad News

- name: Blinding Lights
  artist: The Weeknd
  album: Blinding Lights - Single

# etc.
```