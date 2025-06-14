# Changelog

## 2025-01-14: Initial Implementation

### Created
- **Project Structure**: Set up directory structure with `/api` folder for Vercel
- **Core Server** (`server.py`): Implemented FastMCP server with YouTube transcript fetching
- **OAuth Version** (`server_with_auth.py`): Added optional OAuth authentication support
- **Vercel Handler** (`api/mcp.py`): Created serverless function endpoint
- **Configuration Files**: Added `requirements.txt`, `.gitignore`, `.env.example`
- **Deployment Config** (`vercel.json`): Configured for Python runtime with CORS

### Features Implemented
- Video ID extraction from multiple YouTube URL formats
- Transcript fetching with language prioritization (English > auto-generated > any)
- Optional timestamp inclusion in MM:SS format
- List available transcripts for any video
- Comprehensive error handling
- OAuth authentication support (optional)
- Health check endpoint

### Documentation
- Comprehensive README with features, installation, deployment instructions
- Quick deployment guide with step-by-step Vercel instructions
- Local testing script for validation before deployment
- Environment variable examples

### Technical Decisions
- Used FastMCP for simplified MCP server implementation
- Chose Vercel for hosting (free tier, easy deployment)
- Implemented streamable-http transport for web compatibility
- Added CORS headers for Claude browser integration
- Made OAuth optional for easier initial setup