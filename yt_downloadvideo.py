from pytube import YouTube

url = input("Coloque URL del Video: ")

video = YouTube(url)

video.streams.filter(progressive=True, file_extension="mp4")
stream = video.streams.get_highest_resolution()
stream.download()
