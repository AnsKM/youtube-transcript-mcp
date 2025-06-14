#!/usr/bin/env python3
"""
Test the core functions directly without the MCP server wrapper.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from server import extract_video_id

# Test video URLs
TEST_URLS = [
    ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://www.youtube.com/embed/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("invalid-url", None),
]

def test_video_id_extraction():
    """Test video ID extraction."""
    print("Testing Video ID Extraction:")
    print("-" * 50)
    
    for url, expected in TEST_URLS:
        result = extract_video_id(url)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {url}")
        print(f"  Expected: {expected}, Got: {result}")
    print()

def test_transcript_api():
    """Test YouTube Transcript API directly."""
    print("Testing YouTube Transcript API:")
    print("-" * 50)
    
    # Use a popular video that likely has transcripts
    test_video_id = "dQw4w9WgXcQ"
    
    try:
        # List available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(test_video_id)
        print(f"Available transcripts for video {test_video_id}:")
        
        for transcript in transcript_list:
            type_str = "Manual" if not transcript.is_generated else "Auto-generated"
            print(f"  - {transcript.language} ({transcript.language_code}) - {type_str}")
        
        # Try to fetch English transcript
        print("\nFetching English transcript...")
        try:
            transcript = transcript_list.find_transcript(['en'])
            data = transcript.fetch()
            print(f"Successfully fetched {len(data)} transcript entries")
            if data:
                print(f"First entry: {data[0]}")
        except Exception as e:
            print(f"Could not fetch English transcript: {e}")
            
    except Exception as e:
        print(f"Error accessing transcript API: {e}")
        print("\nThis might happen if:")
        print("- The video doesn't have captions")
        print("- The video is private or deleted")
        print("- YouTube API is temporarily unavailable")

def main():
    """Run all tests."""
    print("YouTube Transcript MCP Server - Function Tests")
    print("=" * 50)
    print()
    
    test_video_id_extraction()
    test_transcript_api()
    
    print("\n" + "=" * 50)
    print("Function tests complete!")
    print("\nNext steps:")
    print("1. Run 'python test_server.py' to test the full MCP server")
    print("2. Use 'npx @fastmcp/inspector python server.py' for interactive testing")

if __name__ == "__main__":
    main()