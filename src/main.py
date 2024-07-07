import locale

from pytube import YouTube

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def format_views(views):
    # Format the views number with thousands separators
    return locale.format_string("%d", views, grouping=True)


def preview(url):
    yt = YouTube(url)
    return yt.author, yt.title, format_views(yt.views)


def download_video(url, file_format=".mp4"):
    yt = YouTube(url)

    if file_format == ".mp4":
        video_stream = yt.streams.filter(only_audio=False).first()
    elif file_format == ".mp3":
        video_stream = yt.streams.filter(only_audio=True).first()
    else:
        raise ValueError("Invalid file format")

    video_stream.download(filename=f'{yt.author} {yt.title}{file_format}')

    print(f"File saved as '{yt.author} {yt.title}{file_format}'")
    return yt.author, yt.title, format_views(yt.views)
