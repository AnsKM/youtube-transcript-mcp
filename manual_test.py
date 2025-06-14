#!/usr/bin/env python3
"""
Manual test of the YouTube transcript functionality.
"""

from youtube_transcript_api import YouTubeTranscriptApi

def test_youtube_transcript():
    """Manually test fetching a YouTube transcript."""
    # Test with Rick Astley - Never Gonna Give You Up
    video_id = "dQw4w9WgXcQ"
    
    print(f"Testing with video ID: {video_id}")
    print("URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("-" * 50)
    
    try:
        # Get transcript
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Get English transcript
        transcript = transcript_list.find_transcript(['en'])
        data = transcript.fetch()
        
        print(f"Language: {transcript.language} ({transcript.language_code})")
        print(f"Type: {'Manual' if not transcript.is_generated else 'Auto-generated'}")
        print(f"Total entries: {len(data)}")
        print("\nFirst 5 entries with timestamps:")
        print("-" * 50)
        
        for i, entry in enumerate(data[:5]):
            seconds = int(entry.start)
            minutes = seconds // 60
            seconds = seconds % 60
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            print(f"{timestamp} {entry.text}")
            
        print("\n✓ Transcript fetching works correctly!")
        
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    test_youtube_transcript()