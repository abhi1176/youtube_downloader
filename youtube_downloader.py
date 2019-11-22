
import os
import sys

from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor, as_completed
from pytube import YouTube, Playlist


def download_youtube_video(link, folder, file_name=None):
	try:
		os.makedirs(folder)
	except:
		pass
	YouTube(link).streams.filter(progressive=True, file_extension='mp4').\
				order_by('resolution').desc().first().download(
					output_path=folder,
					filename=file_name)


def download_youtube_playlist(link, folder=None):
	p = Playlist(link)
	title = p.title()
	if folder:
		folder = os.path.join(folder, title)
	else:
		folder = title
	print(f"Folder to the playlist - {link}: {folder}")
	try:
		os.makedirs(folder)
	except:
		pass
	p.download_all(download_path=folder)


def download_list(filename, folder=None):
	with ThreadPoolExecutor() as executor:
		with open(filename) as f:
			for line in f:
				if not line.strip():
					continue
				if line.startswith("playlist"):
					link = line.strip('playlist').strip().strip(":")
					downloader = download_youtube_playlist
				else:
					link = line.strip()
					downloader = download_youtube_video
				executor.submit(downloader, link, folder)


if __name__ == "__main__":
	parser = ArgumentParser()

	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-l', "--link", help="URL of youtube video or playlist")
	group.add_argument('--urls-file', help="Location of file containing urls")

	parser.add_argument('-d', "--directory",
		help="Directory where you want the video/playlist to be downloaded")
	'''
	file-name and playlist are mutually exclusive
	as the file-name is not applicable to the playlist
	'''
	group2 = parser.add_mutually_exclusive_group()
	group2.add_argument('-f', "--file-name", help="File to be named as?")
	group2.add_argument('-p', "--playlist", action='store_true',
						help="If set, downloads complete playlist")
	args = parser.parse_args()

	if args.urls_file and (args.file_name or args.playlist):
		print("--urls-file and --file-name|--playlist are mutually exclusive")
		sys.exit(2)

	if args.urls_file:
		print(f"Downloading urls in file: {args.urls_file}")
		download_list(args.urls_file, args.directory)
	elif args.playlist:
		print("Downloading playlist!!!")
		download_youtube_playlist(args.link, args.directory)
		print("Done downloading playist!!")
	else:
		print("Downloading video!!")
		download_youtube_video(args.link, args.directory, args.file_name)
		print("Done downloading video!")

'''
python youtube_downloader.py \
	-l "https://www.youtube.com/watch?v=TtIJEQ6D9DE&list=PL-osiE80TeTvviVL0pJGX5mZCo7CAvIuf" \
	--playlist
'''