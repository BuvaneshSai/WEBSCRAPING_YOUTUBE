from pytube import YouTube

link = input("Enter link of youtube videos: ")
yt = YouTube(link)

print("Title : ", yt.title)

print("Views : ", yt.views)

print("Duration :", yt.length)

print("Discription :", yt.description)

print("rating ;", yt.rating)

stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Completed")
