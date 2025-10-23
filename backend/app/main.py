from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import yt_dlp

app = FastAPI(title="Universal Media Downloader API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/process")
async def process_link(request: Request):
    data = await request.json()
    url = data.get("url")

    if not url:
        return JSONResponse({"error": "No URL provided"}, status_code=400)

    try:
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        formats = []
        for f in info.get("formats", []):
            if f.get("url") and f.get("ext") in ["mp4", "webm", "m4a", "mp3"]:
                formats.append({
                    "quality": f.get("format_note") or f.get("height"),
                    "ext": f.get("ext"),
                    "download_url": f.get("url")
                })

        return {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "formats": formats
        }

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Media Downloader</title>
        </head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 100px;">
            <h1>Media Downloader</h1>
            <p>Enter a video URL below to download:</p>
            <form action="/download" method="get">
                <input type="text" name="url" placeholder="Paste URL here" style="width:300px; padding:8px;">
                <button type="submit" style="padding:8px;">Download</button>
            </form>
        </body>
    </html>
    """
