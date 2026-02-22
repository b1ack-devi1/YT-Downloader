# YouTube Downloader CLI Tool

A terminal-based YouTube downloader built with [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
List all available video/audio formats of a YouTube video and download in your chosen format.

Created by: [@b1ack-devi1](https://github.com/b1ack-devi1)


## Features

- List all available formats (video/audio) with details like resolution, size, bitrate.
- Download any format by providing the `Format ID`.
- Save to any folder you choose.
-  Works in terminal (cross-platform).


## Preview

```bash
🔗 Enter YouTube URL : https://www.youtube.com/watch?v=dQw4w9WgXcQ

Available formats for: Rick Astley - Never Gonna Give You Up (Video)

Format ID  Ext    Resolution   Size (MB)  Bitrate    Note
249        webm   audio        1.23       50kbps     
18         mp4    360x240      5.23       145kbps    medium
137        mp4    1080p        90.76      1500kbps   hd1080
...
❓ Enter the Format ID : 137
📁 Enter the folder path to save the video (default: current dir): videos

📥 Downloading 'Rick Astley - Never Gonna Give You Up (Video)' in format 137...
✔️ Download complete!
```

##  Installation
- Clone the repository:	
   ```bash
   git clone https://github.com/b1ack-devi1/YT-Downloader.git
   cd YT-Downloader
   ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Update yt-dlp
  ``` bash
    pip install --upgrade yt-dlp
	```
- Run:
	``` bash
	python yt_d.py
	```
## 🛡️ License

This project is open-source and available under the MIT License.

----------

## Acknowledgements

-   [yt-dlp](https://github.com/yt-dlp/yt-dlp) – Powerful YouTube downloading library
    
-   [Python](https://www.python.org/) – Language used for development
    

----------

## 🌐 Connect
  
🔗 GitHub: [@b1ack-devi1](https://github.com/b1ack-devi1)
