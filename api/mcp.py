"""
Vercel serverless function endpoint for the YouTube Transcript MCP server.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path so we can import our server
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import server components
from server import mcp

# Create the ASGI app for Vercel
app = mcp.get_asgi_app(
    transport="streamable-http",
    path="/mcp"
)

# Vercel expects the app to be named 'app' or 'handler'
handler = app