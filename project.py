import youtube_dl
import os

ydl_opts = {
    'outtmpl': '%(id)s' + '.mp3',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=cnPAYzFI7hE'])

file = 'cnPAYzFI7hE.mp3'
os.system(file)

