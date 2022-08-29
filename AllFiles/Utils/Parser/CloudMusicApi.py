import requests
import json

# ==========================
import SpiderUtils.Search as Searcher
from SpiderUtils.MusicSourceURL import GetSongSourceUrlDefault


def Search(page, limit, question):
    return Searcher.search(page, limit, question)

def Get_source_URL(SongID):
    GetSongSourceUrlDefault(SongId=SongID)