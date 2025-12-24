from pytubefix import YouTube

link ="https://www.youtube.com/watch?v=fXP939XsbO4"
youtube_1 = YouTube(link)

# print(youtube_1.title) to get the title of the link
# print(youtube_1.thumbnail_url) to get the thumbnail

# for streaming

# videos = youtube_1.streams.all() # this is for all format

videos = youtube_1.streams.filter(only_audio=True) # only for audio
vid  =list(enumerate(videos))# we are goint to use list so enumerate gives each character a number

for i in vid:
    print(i)

print()
streaming = int(input("Enter the number: "))
videos[streaming].download()
print("Successfully Downloaded.")

# above code is for a single video

# ****** For playlist ************
# from pytubefix import Playlist

# py = Playlist("https://www.youtube.com/watch?v=abCXAUnQfYU&list=PL9bw4S5ePsEFzl614oAczl-TfI5d4zLHj")
# print(f"Downloading : {py.title}")


# for video in py.videos:
#     video.streams.first().download()