#!/usr/bin/env python3
"""
Local testing script for the YouTube Transcript MCP Server.
Run this to test the server functionality before deployment.
"""

import asyncio
from server import extract_video_id

# Test video URLs
TEST_URLS = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Standard URL
    "https://youtu.be/dQw4w9WgXcQ",                 # Short URL
    "dQw4w9WgXcQ",                                   # Just the ID
    "https://www.youtube.com/embed/dQw4w9WgXcQ",    # Embed URL
    "invalid-url",                                    # Invalid
]

def test_video_id_extraction():
    """Test video ID extraction from various URL formats."""
    print("Testing Video ID Extraction:")
    print("-" * 50)
    
    for url in TEST_URLS:
        video_id = extract_video_id(url)
        print(f"Input: {url}")
        print(f"Extracted ID: {video_id}")
        print()

def test_transcript_fetching():
    """Test fetching transcripts."""
    print("\nTesting Transcript Fetching:")
    print("-" * 50)
    
    # Test with a known video (you may need to change this to a video you know has transcripts)
    test_video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    # Test with timestamps
    print("1. Fetching with timestamps:")
    result = get_youtube_transcript(test_video, include_timestamps=True)
    print(result[:500] + "..." if len(result) > 500 else result)
    print()
    
    # Test without timestamps
    print("2. Fetching without timestamps:")
    result = get_youtube_transcript(test_video, include_timestamps=False)
    print(result[:500] + "..." if len(result) > 500 else result)
    print()
    
    # Test with specific language
    print("3. Fetching with specific language (Spanish):")
    result = get_youtube_transcript(test_video, language="es")
    print(result[:500] + "..." if len(result) > 500 else result)
    print()

def test_list_transcripts():
    """Test listing available transcripts."""
    print("\nTesting List Available Transcripts:")
    print("-" * 50)
    
    test_video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = list_available_transcripts(test_video)
    print(result)

def test_error_handling():
    """Test error handling."""
    print("\nTesting Error Handling:")
    print("-" * 50)
    
    # Test with invalid URL
    print("1. Invalid URL:")
    result = get_youtube_transcript("not-a-valid-url")
    print(result)
    print()
    
    # Test with non-existent video
    print("2. Non-existent video:")
    result = get_youtube_transcript("XXXXXXXXXXXX")
    print(result)
    print()

def main():
    """Run all tests."""
    print("YouTube Transcript MCP Server - Local Testing")
    print("=" * 50)
    
    test_video_id_extraction()
    
    try:
        test_transcript_fetching()
    except Exception as e:
        print(f"Transcript fetching test failed: {e}")
    
    try:
        test_list_transcripts()
    except Exception as e:
        print(f"List transcripts test failed: {e}")
    
    test_error_handling()
    
    print("\n" + "=" * 50)
    print("Testing complete!")
    print("\nNext steps:")
    print("1. Run 'python server.py' to start the server")
    print("2. Use 'npx @fastmcp/inspector python server.py' for interactive testing")
    print("3. Deploy to Vercel when ready")

if __name__ == "__main__":
    main()