import os

import pandas as pd
import yaml

from idunn.console import Console

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

def run(input_file: str, console: Console) -> None:
    """
    Loads data from the input file, converts it, and writes the output file.
    """
    # Validate input first.
    root, ext = os.path.splitext(input_file)
    if ext != '.txt':
        console.warning(f"The input file {input_file} does not have a .txt extension. Are you sure it's the right file?")

    playlist_name = os.path.basename(root)

    if not playlist_name:
        raise ValueError(f'I could not determine the playlist name from {input_file}. I expect a filename like "playlist.txt"')

    # Start doing fun stuff.
    dataframe = _load_tsv(input_file)
    console.info(f'I done loaded the data from {input_file}.')

    songs = list(dataframe.apply(_to_song, axis=1))

    # No more vectorized code past here.
    # Playlists are expected to be small (fewer than 1000 rows).
    playlist = {
        'name': playlist_name,
        'songs': songs
    }

    console.info(f'I done collected the playlist data.')

    yaml_file = f'{playlist_name}.yml'
    if (os.path.exists(yaml_file)):
        raise ValueError(f'The output file {yaml_file} already exists. Please move or remove it before trying again.')

    with open(yaml_file, 'w', encoding='utf-8') as output_file:
        # Since 3.6, dictionaries retain the insertion order of their elements.
        # (Undocumented in 3.6, guaranteed in 3.7)
        # So, we just have to set `sort_keys=False` to keep the order.
        yaml.dump(playlist, output_file, encoding='utf-8', sort_keys=False)

    console.info(f'I done wrote the output to {yaml_file}.')