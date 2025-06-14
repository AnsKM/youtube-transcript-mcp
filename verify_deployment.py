#!/usr/bin/env python3
"""
Verify that your Vercel deployment is working correctly.
"""

import requests
import json
import sys

def verify_deployment(base_url):
    """Test the deployed MCP server."""
    # Remove trailing slash if present
    base_url = base_url.rstrip('/')
    
    print(f"Testing deployment at: {base_url}")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check endpoint...")
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                print("✓ Health check passed!")
                print(f"  Response: {data}")
            else:
                print("✗ Health check failed - unexpected response")
        else:
            print(f"✗ Health check failed - Status code: {response.status_code}")
    except Exception as e:
        print(f"✗ Health check failed - Error: {e}")
    
    # Test 2: MCP endpoint
    print("\n2. Testing MCP endpoint...")
    mcp_url = f"{base_url}/mcp"
    try:
        # MCP servers expect POST requests
        response = requests.post(
            mcp_url,
            json={"jsonrpc": "2.0", "method": "initialize", "id": 1, "params": {}},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code in [200, 405, 422]:  # Various possible responses
            print("✓ MCP endpoint is accessible!")
            print(f"  Status code: {response.status_code}")
        else:
            print(f"✗ MCP endpoint error - Status code: {response.status_code}")
    except Exception as e:
        print(f"✗ MCP endpoint error - {e}")
    
    print("\n" + "=" * 50)
    print("Deployment verification complete!")
    print("\nNext steps:")
    print("1. Add this URL to Claude: " + mcp_url)
    print("2. Test with: 'Get transcript from https://www.youtube.com/watch?v=dQw4w9WgXcQ'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_deployment.py <your-vercel-url>")
        print("Example: python verify_deployment.py https://youtube-transcript-mcp.vercel.app")
        sys.exit(1)
    
    verify_deployment(sys.argv[1])