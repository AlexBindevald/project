import youtube_dl
import os
import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input('Enter name:')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

mylist = list(dict.fromkeys(search_results))
musicUrl = []
musicNames = []

for i in mylist:
    ydl_opts = {
        'quiet': True
    }
    video = "http://www.youtube.com/watch?v=" + i
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video, download=False)
        title = info.get('title', None)
        musicUrl.append(i)
        musicNames.append(title)
for i in range(len(musicNames)):
    print(str(i+1) + '. ' + musicNames[i] )
try:
    number = int(input('What song would you like to listen(Enter number before the song name):'))
except:
    print('Wrong')
def download(videoUrl):
    video = "http://www.youtube.com/watch?v=" + videoUrl
    ydl_opts = {
        'outtmpl': 'Song' + '.mp3',
        'restrictfilenames': 'true'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video])
        info = ydl.extract_info(video, download=False)
        title = info.get('title', None)

    file = 'Song.mp3'
    return file

def play_music(file):
    os.system(file)


play_music(download(musicUrl[number - 1]))

