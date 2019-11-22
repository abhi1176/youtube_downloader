# Youtube Downloader
#### Download videos from youtube

Usage:
&nbsp;&nbsp;&nbsp;&nbsp;youtube_downloader.py 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(-l LINK | --urls-file URLS_FILE)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-d DIRECTORY]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-f FILE_NAME | -p]

-d: Directory where you want to save the video or playlist

-l: Specify the url to a youtube video or of a playlist

--urls-file: Specify the path to the file that contains a youtube url per line

-f: Under what name do you want to save the file `[Only applicable when -l is provided]`

--playlist: store_true - If specified, script considers the link provided with '-l' as a link to the playlist `[Only applicable when -l is provided]`


## Download a youtube video
> python youtube_downloader.py -l "https://www.youtube.com/watch?v=s36EMcPph00" -f "Joey and Chandler.mp4" -d "FRIENDS"

This creates a directory 'FRIENDS' under the current directory and downloads the youtube video in the link and save it as "Joey and Chandler.mp4"


## Download a youtube playlist
> python youtube_downloader.py -l "https://www.youtube.com/watch?v=S1fG1WjTAQw&list=PLN1mxegxWPd1klOqh0DQWlJtEpvms2woq" -p

This creates a directory with the name of the playlist (Revival, in this case) and downloads all the videos in the playlist to the directory


## Download all the links mentioned in the text file
> python youtube_downloader --urls-file "to_download.txt" -d "download_here"

Each line of `to_download.txt` is a url to a youtube video.

This creates a folder with name 'download_here' and downloads all the videos in the urls mentioned in the file