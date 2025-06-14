# Deploy with Vercel CLI

If you prefer using the CLI:

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Answer the prompts**:
   - Set up and deploy: **Y**
   - Which scope: (select your account)
   - Link to existing project: **N**
   - Project name: **youtube-transcript-mcp**
   - Directory: **./**
   - Override settings: **N**

The CLI will give you a URL like:
`https://youtube-transcript-mcp-xxx.vercel.app`

## After Deployment

Your deployment URL will be:
- Preview: `https://youtube-transcript-mcp-xxx.vercel.app`
- Production: `https://youtube-transcript-mcp.vercel.app`

Test it by visiting the root URL. You should see:
```json
{"status": "ok", "server": "YouTube Transcript MCP Server"}
```

The MCP endpoint will be at:
`https://youtube-transcript-mcp.vercel.app/mcp`