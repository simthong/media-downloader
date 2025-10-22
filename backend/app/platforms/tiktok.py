def download_tiktok(url: str, quality: str):
    return {
        "platform": "TikTok",
        "url": url,
        "quality": quality,
        "download_url": f"https://example.com/download/tiktok/{quality}"
    }
