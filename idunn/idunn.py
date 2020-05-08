import os

import pandas as pd
import yaml

def _load_tsv(filename: str) -> pd.DataFrame:
    """
    Loads a file in TSV format with the expected schema.
    """
    dataframe = pd.read_csv(filename, sep='\t')
    return dataframe[['Name', 'Artist', 'Album']]

def _to_song(row: pd.Series):
    return {
        'name': row.Name,
        'artist': row.Artist,
        'album': row.Album
    }

def run(input_file):
    # TODO log progress to console
    root, _ = os.path.splitext(input_file)
    playlist_name = os.path.basename(root)

    if not playlist_name:
        raise ValueError(f'Could not determine the playlist name from {input_file}. \
            Expecting a filename like "playlist.txt"')

    dataframe = _load_tsv(input_file)
    songs = list(dataframe.apply(_to_song, axis=1))

    # No more vectorized code past here.
    # Playlists are expected to be small (fewer than 1000 rows).
    playlist = {
        'name': playlist_name,
        'songs': songs
    }

    # TODO check if file exists
    with open(f'{playlist_name}.yml', 'w', encoding='utf-8') as output_file:
        yaml.dump(playlist, output_file, encoding='utf-8')