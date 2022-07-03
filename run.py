import yt_dlp

url = input("Youtube Video Link: ")
choice = input(
    "\nDownload Format:\n1 - Audio\n2 - Only Video\n3 - Video with Audio\n\n"
)
if choice == "1":
    ydlp_opts = {
        "outtmpl": "YouTube Downloads/%(title)s.mp3",
        "format": "bestaudio[ext=m4a]/bestaudio",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }
elif choice == "2":
    ydlp_opts = {
        "outtmpl": "YouTube Downloads/%(title)s.mp4",
        "format": "bestvideo[ext=mp4][height<=1080]/bestvideo",
        "writethumbnail": True,
        "postprocessors": [{"key": "FFmpegMetadata"}, {"key": "EmbedThumbnail"}],
    }
else:
    ydlp_opts = {
        "outtmpl": "YouTube Downloads/%(title)s.mp4",
        "format": "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/bestvideo+bestaudio",
        "writesubtitles": True,
        "subtitle": "--write-auto-sub --sub-lang en",
        "writethumbnail": True,
        "postprocessors": [
            {"key": "FFmpegMetadata"},
            {"key": "FFmpegEmbedSubtitle"},
            {"key": "EmbedThumbnail"},
        ],
    }
with yt_dlp.YoutubeDL(ydlp_opts) as ydlp:
    ydlp.download([url.lstrip()])
