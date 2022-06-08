from mhyt import yt_download
print("\nBem-vindo\n")

url = input("Cole a URl do video: ")
file = 'sertanejo.mp3'
yt_download(url, file, ismusic=True)