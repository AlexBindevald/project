import youtube_dl
import os
import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input('Enter name:')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
ydl_opts = {
    'outtmpl': '%(title)s' + '.mp3',
    'restrictfilenames': 'true'
}

video = "http://www.youtube.com/watch?v=" + search_results[5]
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video, download=False)
    url = info.get('url', None)
    id = info.get('id', None)
    title = info.get('title', None)

print(title)
title = title.replace(' ', '_')
file = str(title) + '.mp3'
os.system(file)


