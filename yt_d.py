import os
import subprocess
from yt_dlp import YoutubeDL

def list_formats(url):
    ydl_opts = {
        'quiet': True,
        'forcejson': True,
        'simulate': True,

    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        print(f"\nAvailable formats for: {info['title']}\n")
        print(f"{'Format ID':<10} {'Ext':<6} {'Resolution':<12} {'Size (MB)':<10} {'Bitrate':<10} {'Note'}")
        for f in formats:
            size = f.get('filesize') or f.get('filesize_approx')
            size_mb = f"{round(size / 1024 / 1024, 2)}" if size else "-"
            bitrate = f"{round(f.get('tbr', 0))}kbps" if f.get('tbr') else "-"
            print(f"{f['format_id']:<10} {f['ext']:<6} {f.get('resolution', 'audio'):<12} {size_mb:<10} {bitrate:<10} {f.get('format_note', '')}")  

        return info['title']

def download_format(url, format_id, output_path):
    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("\n ✔️ Download complete!")


def mainRe():
    print(
    "\n 🎥To download another video paste the URL or Ctrl+C to exit.")

    url = input(" \n 🔗 Enter YouTube URL : ").strip()
    title = list_formats(url)

    format_id = input("\n ❓ Enter the Format ID : ").strip()
    output_path = input("\n 📁 Enter the folder path to save the video (default: current dir): ").strip()
    if not output_path:
        output_path = "."

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print(f"\n 📥 Downloading '{title}' in format {format_id}...")
    download_format(url, format_id, output_path)

    mainRe()

def main():
    print(r"""
        __   _______     ____                      _                 _           
        \ \ / /_   _|   |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
         \ V /  | |_____| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
          | |   | |_____| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
          |_|   |_|     |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   

          created by: @b1ack-devi1
                                                                          
    """)
    url = input(" 🔗 Enter YouTube URL : ").strip()
    title = list_formats(url)

    format_id = input("\n ❓ Enter the Format ID : ").strip()
    output_path = input("\n 📁 Enter the folder path to save the video (default: current dir): ").strip()
    if not output_path:
        output_path = "."

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print(f"\n 📥 Downloading '{title}' in format {format_id}...")
    download_format(url, format_id, output_path)


    mainRe()

if __name__ == "__main__":
    main()
