import json
import requests

def search(page,limit,question):
    Url = f"http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={question}&type=1&offset={page}&total=true&limit={limit}"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    ReqPkt = requests.get(Url,headers=headers)
    Json = json.loads(ReqPkt.text)
    output = Json["result"]["songs"][0]
    return output
#tests