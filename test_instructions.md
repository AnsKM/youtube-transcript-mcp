# Testing the YouTube Transcript MCP Server Locally

## Quick Test

1. **Run the server**:
   ```bash
   source venv/bin/activate
   python server.py
   ```

2. **Test with MCP Inspector** (recommended):
   ```bash
   source venv/bin/activate
   npx @fastmcp/inspector python server.py
   ```
   
   This will open a web interface where you can:
   - See available tools: `get_youtube_transcript` and `list_available_transcripts`
   - Test the tools with sample YouTube URLs
   - View the formatted transcript output

## Sample YouTube URLs to Test

1. **Rick Astley - Never Gonna Give You Up**
   - URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Has manual English transcript

2. **Short format**: `https://youtu.be/dQw4w9WgXcQ`

3. **Just the ID**: `dQw4w9WgXcQ`

## Testing the Tools

### get_youtube_transcript
Parameters:
- `video_url`: Any YouTube URL or video ID
- `include_timestamps`: true/false (optional, default: true)
- `language`: Language code like "en", "es" (optional)

Example inputs:
```json
{
  "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "include_timestamps": true
}
```

### list_available_transcripts
Parameters:
- `video_url`: Any YouTube URL or video ID

Example:
```json
{
  "video_url": "dQw4w9WgXcQ"
}
```

## Expected Output

The transcript will include:
- Video ID
- Language and type (manual/auto-generated)
- Formatted transcript with timestamps in [MM:SS] format
- Full text content

## Troubleshooting

If you encounter issues:

1. **Module not found**: Make sure virtual environment is activated
2. **No transcripts**: Try a different video (some videos don't have captions)
3. **API errors**: YouTube might be temporarily unavailable

## Next Steps

Once local testing is successful:
1. Deploy to Vercel using the deployment guide
2. Add to Claude via Settings → Integrations
3. Test in Claude with "Get transcript from [YouTube URL]"