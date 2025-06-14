"""
Simple test endpoint to verify Vercel Python deployment.
"""

def handler(request):
    """Simple handler for testing."""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "status": "ok",
            "message": "Python function is working!"
        }
    }