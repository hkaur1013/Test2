from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def download_youtube_video(video_url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download(output_path)

        print(f"Video '{yt.title}' downloaded successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace the URL with the YouTube video URL you want to download
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Replace the second argument with the desired output path (default is the current directory)
    download_youtube_video(youtube_url)
