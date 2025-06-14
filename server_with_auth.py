#!/usr/bin/env python3
"""
YouTube Transcript MCP Server with OAuth Authentication
A secure Model Context Protocol server that fetches transcripts from YouTube videos.
"""

import os
import re
from typing import Optional, List, Dict, Any
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)
from mcp.server.auth.provider import OAuthAuthorizationServerProvider
from mcp.server.auth.settings import (
    AuthSettings,
    ClientRegistrationOptions,
    RevocationOptions,
)

# Load environment variables
load_dotenv()

class SimpleOAuthProvider(OAuthAuthorizationServerProvider):
    """Simple OAuth provider for demonstration purposes."""
    
    async def get_client_secret(self, client_id: str) -> Optional[str]:
        """Return the client secret for a given client ID."""
        # In production, this would query a database
        if client_id == os.getenv("OAUTH_CLIENT_ID"):
            return os.getenv("OAUTH_CLIENT_SECRET")
        return None
    
    async def save_client_secret(self, client_id: str, client_secret: str) -> None:
        """Save a client secret (not implemented for this demo)."""
        pass
    
    async def save_authorization(
        self,
        authorization_id: str,
        client_id: str,
        scopes: List[str],
        redirect_uri: str,
        state: Optional[str],
        code_challenge: Optional[str],
        code_challenge_method: Optional[str]
    ) -> None:
        """Save authorization details (simplified for demo)."""
        pass
    
    async def get_authorization(
        self,
        authorization_id: str
    ) -> Optional[Dict[str, Any]]:
        """Get authorization details (simplified for demo)."""
        return {
            "client_id": os.getenv("OAUTH_CLIENT_ID"),
            "scopes": ["transcript:read"],
            "redirect_uri": "http://localhost:3000/callback"
        }
    
    async def delete_authorization(self, authorization_id: str) -> None:
        """Delete authorization (not implemented for demo)."""
        pass
    
    async def save_token(
        self,
        token: str,
        client_id: str,
        scopes: List[str],
        expires_at: int
    ) -> None:
        """Save token details (simplified for demo)."""
        pass
    
    async def get_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Get token details (simplified for demo)."""
        return {
            "client_id": os.getenv("OAUTH_CLIENT_ID"),
            "scopes": ["transcript:read"],
            "expires_at": 9999999999  # Far future
        }
    
    async def delete_token(self, token: str) -> None:
        """Delete token (not implemented for demo)."""
        pass

# Initialize the MCP server with authentication
auth_enabled = os.getenv("OAUTH_CLIENT_ID") is not None

if auth_enabled:
    mcp = FastMCP(
        name=os.getenv("MCP_SERVER_NAME", "YouTube Transcript Fetcher"),
        version=os.getenv("MCP_SERVER_VERSION", "1.0.0"),
        auth_server_provider=SimpleOAuthProvider(),
        auth=AuthSettings(
            issuer_url=os.getenv("OAUTH_ISSUER_URL", "https://your-server-url.vercel.app"),
            revocation_options=RevocationOptions(
                enabled=True,
            ),
            client_registration_options=ClientRegistrationOptions(
                enabled=True,
                valid_scopes=["transcript:read"],
                default_scopes=["transcript:read"],
            ),
            required_scopes=["transcript:read"],
        ),
    )
else:
    # No auth mode for local development
    mcp = FastMCP(
        name=os.getenv("MCP_SERVER_NAME", "YouTube Transcript Fetcher"),
        version=os.getenv("MCP_SERVER_VERSION", "1.0.0")
    )

def extract_video_id(url_or_id: str) -> Optional[str]:
    """Extract video ID from YouTube URL or return the ID if already provided."""
    # If it's already just an ID (11 characters)
    if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id
    
    # Try to parse as URL
    try:
        parsed = urlparse(url_or_id)
        
        # Handle youtu.be short URLs
        if parsed.netloc == 'youtu.be':
            return parsed.path.lstrip('/')
        
        # Handle youtube.com URLs
        if parsed.netloc in ['www.youtube.com', 'youtube.com', 'm.youtube.com']:
            if parsed.path == '/watch':
                query = parse_qs(parsed.query)
                return query.get('v', [None])[0]
            elif parsed.path.startswith('/embed/'):
                return parsed.path.split('/')[2]
            elif parsed.path.startswith('/v/'):
                return parsed.path.split('/')[2]
    except:
        pass
    
    return None

def format_transcript(transcript: List[Dict[str, Any]], include_timestamps: bool = True) -> str:
    """Format transcript entries into readable text."""
    if not transcript:
        return "No transcript available."
    
    formatted_lines = []
    for entry in transcript:
        if include_timestamps:
            # Convert seconds to MM:SS format
            seconds = int(entry['start'])
            minutes = seconds // 60
            seconds = seconds % 60
            timestamp = f"[{minutes:02d}:{seconds:02d}]"
            formatted_lines.append(f"{timestamp} {entry['text']}")
        else:
            formatted_lines.append(entry['text'])
    
    return '\n'.join(formatted_lines)

@mcp.tool()
def get_youtube_transcript(
    video_url: str,
    include_timestamps: bool = True,
    language: Optional[str] = None
) -> str:
    """
    Fetch transcript from a YouTube video.
    
    Args:
        video_url: YouTube video URL or video ID
        include_timestamps: Whether to include timestamps in the transcript
        language: Preferred language code (e.g., 'en', 'es'). If not specified, 
                 prioritizes English then falls back to auto-generated.
    
    Returns:
        Formatted transcript text
    """
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Error: Invalid YouTube URL or video ID provided."
    
    try:
        # Get list of available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get transcript based on preferences
        transcript = None
        
        if language:
            # Try to get specific language requested
            try:
                transcript = transcript_list.find_transcript([language])
            except:
                # If specific language not found, we'll try defaults below
                pass
        
        if not transcript:
            # Try to get manually created English transcript first
            try:
                transcript = transcript_list.find_manually_created_transcript(['en'])
            except:
                # Try auto-generated English
                try:
                    transcript = transcript_list.find_generated_transcript(['en'])
                except:
                    # Get any available transcript
                    try:
                        # Get first available transcript
                        for t in transcript_list:
                            transcript = t
                            break
                    except:
                        pass
        
        if not transcript:
            return "Error: No transcripts available for this video."
        
        # Fetch the actual transcript data
        transcript_data = transcript.fetch()
        
        # Format and return
        formatted = format_transcript(transcript_data, include_timestamps)
        
        # Add metadata
        metadata = f"Video ID: {video_id}\n"
        metadata += f"Language: {transcript.language} ({transcript.language_code})\n"
        metadata += f"Type: {'Manual' if not transcript.is_generated else 'Auto-generated'}\n"
        metadata += f"{'=' * 50}\n\n"
        
        return metadata + formatted
        
    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except VideoUnavailable:
        return "Error: Video is unavailable or does not exist."
    except NoTranscriptFound:
        return "Error: No transcript found for this video."
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

@mcp.tool()
def list_available_transcripts(video_url: str) -> str:
    """
    List all available transcripts for a YouTube video.
    
    Args:
        video_url: YouTube video URL or video ID
    
    Returns:
        List of available transcripts with language codes
    """
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Error: Invalid YouTube URL or video ID provided."
    
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        available = []
        for transcript in transcript_list:
            type_str = "Manual" if not transcript.is_generated else "Auto-generated"
            available.append(
                f"- {transcript.language} ({transcript.language_code}) - {type_str}"
            )
        
        if available:
            return f"Available transcripts for video {video_id}:\n" + "\n".join(available)
        else:
            return "No transcripts available for this video."
            
    except Exception as e:
        return f"Error: {str(e)}"

# Add a resource that provides information about the server
@mcp.resource("server_info")
def get_server_info() -> str:
    """Get information about this MCP server."""
    auth_status = "Enabled" if auth_enabled else "Disabled"
    return f"""YouTube Transcript MCP Server

This server provides tools to fetch transcripts from YouTube videos.

Available tools:
1. get_youtube_transcript - Fetch and format video transcripts
2. list_available_transcripts - List all available transcript languages

Features:
- Automatic video ID extraction from various YouTube URL formats
- Prioritizes manual English transcripts over auto-generated
- Falls back to other languages if English unavailable
- Optional timestamp inclusion
- Detailed error messages

Authentication: {auth_status}
"""

if __name__ == "__main__":
    # Run the server
    mcp.run()