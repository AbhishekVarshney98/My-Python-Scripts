from pytube import Playlist
link = input("Enter the link of the playlist:")
# pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")
pl = Playlist(link)
# pl.download_all('/path/to/directory/')
folder = input("Enter folder name")
pl.download_all('C:\\Users\\Asus\\Desktop\\{}'.format(folder))
