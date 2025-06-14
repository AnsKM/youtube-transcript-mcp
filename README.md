# YouTube Transcript MCP Server

A Model Context Protocol (MCP) server that fetches transcripts from YouTube videos. This server can be deployed remotely and integrated with Claude to provide YouTube transcript fetching capabilities directly in your conversations.

## Features

- **Extract transcripts** from any YouTube video with available captions
- **Multiple URL format support** - works with full URLs, short URLs, and video IDs
- **Language prioritization** - automatically selects English transcripts, falls back to auto-generated
- **Timestamp inclusion** - optional timestamps in MM:SS format
- **OAuth authentication** - secure access control (optional)
- **Error handling** - clear error messages for common issues

## Prerequisites

- Python 3.8 or higher
- A Vercel account (for deployment)
- Claude Pro/Max/Team/Enterprise subscription (for MCP integration)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd youtube-transcript-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy the environment file:
```bash
cp .env.example .env
```

4. (Optional) Configure OAuth settings in `.env` if you want authentication.

## Local Testing

### Basic Server (No Auth)

Run the server locally:
```bash
python server.py
```

To test with MCP Inspector:
```bash
npx @fastmcp/inspector python server.py
```

### Server with Authentication

Run the authenticated version:
```bash
python server_with_auth.py
```

## Deployment to Vercel

### 1. Prepare for Deployment

Ensure your project has these files:
- `api/mcp.py` - Vercel handler
- `vercel.json` - Deployment configuration
- `requirements.txt` - Python dependencies
- `server.py` - Main server code

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Follow the prompts
```

#### Option B: Using GitHub Integration

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Add New Project"
4. Import your GitHub repository
5. Configure environment variables (if using OAuth)
6. Deploy

### 3. Set Environment Variables

In Vercel dashboard, add these environment variables if using OAuth:
- `OAUTH_CLIENT_ID`
- `OAUTH_CLIENT_SECRET`
- `OAUTH_ISSUER_URL` (your Vercel deployment URL)

## Integration with Claude

1. Go to Claude settings → Integrations
2. Click "Add custom integration"
3. Enter your Vercel deployment URL: `https://your-app.vercel.app/mcp`
4. Complete the OAuth flow (if enabled)
5. The YouTube transcript tools are now available!

## Usage in Claude

Once integrated, you can use these commands in Claude:

### Fetch a transcript:
```
"Get the transcript from https://www.youtube.com/watch?v=VIDEO_ID"
```

### List available languages:
```
"What transcript languages are available for this video?"
```

### Get transcript without timestamps:
```
"Get the transcript without timestamps"
```

### Specify a language:
```
"Get the Spanish transcript for this video"
```

## Available Tools

### 1. `get_youtube_transcript`
Fetches and formats the transcript from a YouTube video.

**Parameters:**
- `video_url` (required): YouTube URL or video ID
- `include_timestamps` (optional): Include timestamps (default: true)
- `language` (optional): Preferred language code (e.g., 'en', 'es')

### 2. `list_available_transcripts`
Lists all available transcript languages for a video.

**Parameters:**
- `video_url` (required): YouTube URL or video ID

## Error Handling

The server provides clear error messages for common issues:
- Invalid YouTube URL or video ID
- Transcripts disabled for the video
- Video unavailable or doesn't exist
- No transcripts found
- Language not available

## Security Considerations

### For Production Use:
1. **Enable OAuth authentication** by setting environment variables
2. **Restrict CORS origins** to Claude domains only
3. **Implement rate limiting** to prevent abuse
4. **Monitor usage** through Vercel analytics

### OAuth Setup (Optional)

For enhanced security, configure OAuth:

1. Set these environment variables:
   - `OAUTH_CLIENT_ID`: Your OAuth client ID
   - `OAUTH_CLIENT_SECRET`: Your OAuth client secret
   - `OAUTH_ISSUER_URL`: Your deployment URL

2. The server will automatically enable OAuth when these are set.

## Troubleshooting

### Common Issues:

1. **"No module named 'fastmcp'"**
   - Run: `pip install -r requirements.txt`

2. **Vercel deployment fails**
   - Check Node.js version is 18.x in Vercel settings
   - Ensure all files are committed to git

3. **OAuth errors**
   - Verify environment variables are set correctly
   - Check OAUTH_ISSUER_URL matches your deployment

4. **Transcript not found**
   - Video may not have captions enabled
   - Try a different video to test

## Development

### Project Structure:
```
youtube-transcript-mcp/
├── api/
│   └── mcp.py          # Vercel handler
├── server.py           # Basic MCP server
├── server_with_auth.py # OAuth-enabled server
├── requirements.txt    # Dependencies
├── vercel.json        # Vercel config
├── .env.example       # Environment template
├── .gitignore         # Git ignore file
└── README.md          # Documentation
```

### Adding New Features:

1. Modify `server.py` to add new tools
2. Test locally with MCP Inspector
3. Update documentation
4. Deploy to Vercel

## Cost Analysis

### Vercel (Recommended)
- **Free Tier**: 100GB bandwidth, 100 hours compute
- **Sufficient for**: Personal use, ~10,000 transcript fetches/month
- **Upgrade**: Pro plan at $20/month for more resources

### Alternative Hosting:
- **Deta**: Free forever, good for light use
- **PythonAnywhere**: Free tier with limitations
- **Google Cloud Run**: Pay-per-use after free tier

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
- Create an issue on GitHub
- Check existing issues for solutions
- Review Claude MCP documentation

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp)
- Uses [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- Deployed on [Vercel](https://vercel.com)

## Deployment Status

[![Deployed on Vercel](https://vercel.com/button)](https://youtube-transcript-mcp.vercel.app)
