class GetSongSourceUrlDefault():
    def __init__(self, SongId):
        Url = f"http://music.163.com/song/media/outer/url?id={SongId}.mp3"
        return Url