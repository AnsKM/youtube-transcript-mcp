#!/usr/bin/env python3
"""
Simple test script to verify the server works locally.
"""

import subprocess
import sys

print("YouTube Transcript MCP Server - Local Test")
print("=" * 50)
print()
print("Starting the MCP server...")
print("This will open the MCP Inspector in your browser.")
print()
print("To test the server:")
print("1. In the Inspector, find the 'get_youtube_transcript' tool")
print("2. Enter a YouTube URL like: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("3. Click 'Run Tool' to fetch the transcript")
print()
print("Press Ctrl+C to stop the server.")
print()

# Run the server
try:
    subprocess.run([sys.executable, "server.py"], check=True)
except KeyboardInterrupt:
    print("\nServer stopped.")
except subprocess.CalledProcessError as e:
    print(f"Error running server: {e}")