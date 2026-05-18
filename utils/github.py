import requests
import re

def fetch_github_code(url):
    """
    Accepts a GitHub file URL and returns the raw code content
    Example URL: https://github.com/user/repo/blob/main/file.py
    """
    try:
        # Convert normal GitHub URL to raw URL
        if "github.com" in url and "blob" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com")
            raw_url = raw_url.replace("/blob/", "/")
        elif "raw.githubusercontent.com" in url:
            raw_url = url
        else:
            return None, "❌ Invalid GitHub URL! Please paste a valid GitHub file URL."

        # Fetch the code
        response = requests.get(raw_url)

        if response.status_code == 200:
            return response.text, None
        else:
            return None, f"❌ Could not fetch file. Status code: {response.status_code}"

    except Exception as e:
        return None, f"❌ Error fetching code: {str(e)}"


def is_github_url(text):
    """Check if the text is a GitHub URL"""
    pattern = r'https?://(github\.com|raw\.githubusercontent\.com)/.+'
    return bool(re.match(pattern, text.strip()))