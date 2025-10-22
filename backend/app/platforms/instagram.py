def download_instagram(url: str, quality: str):
    return {
        "platform": "Instagram",
        "url": url,
        "quality": quality,
        "download_url": f"https://example.com/download/instagram/{quality}"
    }
