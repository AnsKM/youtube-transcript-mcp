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

# Create the handler for Vercel
# FastMCP will automatically create the appropriate ASGI app when using streamable-http
handler = mcp.get_asgi_app(
    transport="streamable-http",
    path="/mcp"
)

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(handler, host="0.0.0.0", port=8000)