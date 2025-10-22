def download_snapchat(url: str, quality: str):
    return {
        "platform": "Snapchat",
        "url": url,
        "quality": quality,
        "download_url": f"https://example.com/download/snapchat/{quality}"
    }
