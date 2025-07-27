# YT-Downloader

A simple Python command-line script to **list and download YouTube video/audio formats** using the powerful [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library.

---

## ✅ Features

- List **all available formats** (video & audio) of a YouTube video
- Download selected format by Format ID
- Save video/audio in **custom output folder**
- Automatically names files based on video title

---
```pgsql
🎥 Enter YouTube URL: https://www.youtube.com/watch?v=abcd1234

Available formats for: Example Video Title

Format ID  Ext    Resolution   Note
18         mp4    360p         medium
22         mp4    720p         hd
140        m4a    audio        audio only

🎯 Enter the Format ID you want to download: 140
📁 Enter the folder path to save the video (default: current dir): downloads

📥 Downloading 'Example Video Title' in format 140...
✅ Download complete!
```


## 📦 Requirements

- Python 3.6+
- `yt-dlp` library

Install dependencies:
```bash
pip install yt-dlp

