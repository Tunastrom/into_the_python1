import youtube_dl

ydl_opt = {
    'format': 'best[height<=480]',
    'outtmpl': '%(title)s %(resolution)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Yb874XxG73c'])