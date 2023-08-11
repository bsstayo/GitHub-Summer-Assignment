import requests
from bs4 import BeautifulSoup
from datetime import datetime

melon_page_req = requests.get(
    "https://www.melon.com/chart/index.htm",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    },
)
content = melon_page_req.content.decode('utf-8','replace')
soup = BeautifulSoup(content, "html.parser")
song_infos = soup.select(".wrap_song_info")
today = datetime.today().strftime("%Y%m%d%H%M%S")
print(today)

new_file = open(f'{today[0:4]}년 {today[4:6]}월 {today[6:8]}일자 top 100.txt', "w+", encoding='utf-8')
for i in range(0, 20, 2):
    tmp = song_infos[i].find_all("div")

    title = tmp[0].span.a.text
    artist = tmp[1].span.a.text
    album = song_infos[i + 1].div.a.text
    new_file.write(f'제목: {title}  |  아티스트: {artist}  |  앨범: {album}\n')
new_file.close()