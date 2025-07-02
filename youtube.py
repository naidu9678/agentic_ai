from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable, NoTranscriptFound
import re

def get_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.
    """
    video_id_match = re.search(r"v=([\w-]{11})", youtube_url)
    if not video_id_match:
        raise ValueError("Invalid YouTube URL format. Unable to extract video ID.")
    return video_id_match.group(1)

def fetch_youtube_transcript(url):
    """
    Fetches the transcript for a YouTube video given its URL.
    """
    try:
        video_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry["text"] for entry in transcript])
        return transcript_text
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except VideoUnavailable:
        return "The video is unavailable."
    except NoTranscriptFound:
        return "No transcript found for this video."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    transcript = fetch_youtube_transcript(youtube_url)
    print("\nTranscript:")
    print(transcript)
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable, NoTranscriptFound
import re

def get_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.
    """
    video_id_match = re.search(r"v=([\w-]{11})", youtube_url)
    if not video_id_match:
        raise ValueError("Invalid YouTube URL format. Unable to extract video ID.")
    return video_id_match.group(1)

def fetch_youtube_transcript(url):
    """
    Fetches the transcript for a YouTube video given its URL.
    """
    try:
        video_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry["text"] for entry in transcript])
        return transcript_text
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except VideoUnavailable:
        return "The video is unavailable."
    except NoTranscriptFound:
        return "No transcript found for this video."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    transcript = fetch_youtube_transcript(youtube_url)
    print("\nTranscript:")
    print(transcript)

