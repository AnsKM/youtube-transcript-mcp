# Quick Deployment Guide

This guide will help you deploy your YouTube Transcript MCP server to Vercel in minutes.

## Prerequisites

- GitHub account
- Vercel account (free)
- Node.js installed (for Vercel CLI)

## Step-by-Step Deployment

### 1. Prepare Your Code

First, make sure all files are ready:
```bash
# Test locally first
python test_local.py

# If tests pass, check file structure
ls -la
```

You should have:
- `api/mcp.py`
- `server.py`
- `requirements.txt`
- `vercel.json`

### 2. Create GitHub Repository

```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial YouTube Transcript MCP server"

# Create repo on GitHub and push
# Follow GitHub's instructions to create a new repository
git remote add origin https://github.com/YOUR_USERNAME/youtube-transcript-mcp.git
git push -u origin main
```

### 3. Deploy to Vercel

#### Option A: Via Vercel Dashboard (Easiest)

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Select "Import Git Repository"
4. Choose your GitHub repo
5. Vercel will auto-detect the configuration
6. Click "Deploy"

#### Option B: Via CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Answer the prompts:
# - Set up and deploy: Y
# - Which scope: (select your account)
# - Link to existing project: N
# - Project name: youtube-transcript-mcp (or your choice)
# - Directory: ./
# - Override settings: N
```

### 4. Get Your URL

After deployment, you'll get a URL like:
```
https://youtube-transcript-mcp-xxx.vercel.app
```

Test it by visiting:
```
https://youtube-transcript-mcp-xxx.vercel.app/
```

You should see: `{"status":"ok","server":"YouTube Transcript MCP Server"}`

### 5. Add to Claude

1. Open Claude in your browser
2. Go to Settings → Integrations
3. Click "Add custom integration"
4. Enter your MCP endpoint URL:
   ```
   https://youtube-transcript-mcp-xxx.vercel.app/mcp
   ```
5. Click "Add"

### 6. Test in Claude

Try these prompts:
- "Get the transcript from https://www.youtube.com/watch?v=dQw4w9WgXcQ"
- "List available transcripts for youtube.com/watch?v=dQw4w9WgXcQ"

## Troubleshooting

### Deployment Fails

1. Check Node.js version in Vercel:
   - Go to Project Settings → General
   - Change Node.js Version to 18.x

2. Check logs:
   - Go to Functions tab in Vercel dashboard
   - Check for error messages

### Integration Doesn't Work

1. Make sure URL ends with `/mcp`
2. Check CORS is enabled (it is in our config)
3. Try refreshing Claude page

### No Transcripts Found

Some videos don't have captions. Try these test videos that definitely have transcripts:
- TED Talks
- Official music videos
- Educational content

## Environment Variables (Optional)

For OAuth (advanced users):

1. Go to Vercel Project Settings → Environment Variables
2. Add:
   - `OAUTH_CLIENT_ID`
   - `OAUTH_CLIENT_SECRET`
   - `OAUTH_ISSUER_URL` (your Vercel URL)
3. Redeploy

## Monitoring

Check your usage:
1. Vercel Dashboard → Analytics
2. Monitor:
   - Function invocations
   - Bandwidth usage
   - Error rate

Free tier limits:
- 100GB bandwidth/month
- 100 hours compute/month

## Updates

To update your server:

```bash
# Make changes
git add .
git commit -m "Update: description of changes"
git push

# Vercel auto-deploys from GitHub
```

## Support

- Check Vercel logs for errors
- Test locally first with `python test_local.py`
- Use MCP Inspector for debugging: `npx @fastmcp/inspector python server.py`

That's it! Your YouTube Transcript MCP server is now live and integrated with Claude.