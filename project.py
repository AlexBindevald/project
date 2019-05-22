import youtube_dl
import os
import urllib.request
import urllib.parse
from tkinter import *
fields = 'Song name', 'Song number'
musicUrl = []
def searchSong(songname):
    musicList = ""
    del musicUrl[:]
    output.delete('1.0', END)
    query_string = urllib.parse.urlencode({"search_query": songname})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

    mylist = list(dict.fromkeys(search_results))
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
        musicList += str(i + 1) + '. ' + musicNames[i] + '\n'
    output.insert(INSERT, musicList)
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
def play(entries):
    for entry in entries:
        if(entry[0] == 'Song number'):
            number = entry[1].get()
            if(os.path.isfile('./Song.mp3')):
                os.remove(r'C:\Users\test\PycharmProjects\untitled\project\Song.mp3')
            play_music(download(musicUrl[int(number) - 1]))
def fetch(entries):
   for entry in entries:
       if(entry[0] == 'Song name'):
           text = entry[1].get()
           searchSong(text)



def makeform(root, fields):
   entries = []
   for field in fields:
       row = Frame(root)
       lab = Label(row, width=15, text=field, anchor='w')
       ent = Entry(row)
       row.pack(side=TOP, fill=X, padx=5, pady=5)
       lab.pack(side=LEFT)
       ent.pack(side=RIGHT, expand=YES, fill=X)
       entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   count = 0
   ents = makeform(root, fields)
   output = Text(root, width=100, height=30, background="light grey")
   output.pack()
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Search song',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b1 = Button(root, text='Play song',
               command=(lambda e=ents: play(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

# try:
#     number = int(input('What song would you like to listen(Enter number before the song name):'))
# except:
#     print('Wrong')

# play_music(download(musicUrl[number - 1]))


