# Requirements - In cmd run these lines
#pip install youtube_dl
#For linux users, use this to get Convertion feature too : sudo apt-get install ffmpeg

#This program reads list of youtube urls in each line of .txt file as input, hence a file named "List_of_Youtube_URL.txt" is needed.
from __future__ import unicode_literals
import youtube_dl

def read_url():
    fp = open("List_of_Youtube_URL.txt", 'r')
    URL = fp.read().split('\n')
    return URL
#Mess around with ydl_opts for changing download file format
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
count_downloaded = 0
#Replace ydl.download(['XXXXX'] with url of file
url_list=read_url()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for each_url in url_list:
		try:
			ydl.download([each_url])
		except:
			pass
		count_downloaded += 1
if count_downloaded > 0:
	print 'Downloading of ' + str(count_downloaded) + ' videos completed successfully!'