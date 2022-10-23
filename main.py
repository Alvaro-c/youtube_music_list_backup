from ytmusicapi import YTMusic


def main():
    # YTMusic.setup(filepath='headers_auth.json')
    yt = YTMusic("headers_auth.json")

    total_songs = yt.get_liked_songs()
    total_songs = total_songs['trackCount']

    liked_songs = yt.get_liked_songs(total_songs)
    for i, song in enumerate(liked_songs['tracks']):
        title = ""
        list_of_artists = ""
        album = ""
        duration = ""
        youtube_music_link = ""
        youtube_link = ""

        internal_id = len(liked_songs['tracks']) - i
        if song['title']:
            title = song['title']

        if song['artists']:
            for j, artist in enumerate(song['artists']):
                if j == 0:
                    list_of_artists = artist['name']
                else:
                    list_of_artists = f"{list_of_artists} & {artist['name']}"

        if song['album']:
            album = song['album']['name']

        if song['duration']:
            duration = song['duration']

        if song['videoId']:
            youtube_music_link = f"https://music.youtube.com/watch?v={song['videoId']}"
            youtube_link = f"https://www.youtube.com/watch?v={song['videoId']}"
        print(
            f"{internal_id};{title};{list_of_artists};{album};{duration};"
            f"{youtube_music_link};{youtube_link}")


if __name__ == '__main__':
    main()
