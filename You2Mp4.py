import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os
from string import ascii_letters, digits

def clean_video_title(title):
    valid_chars = "-_.() %s%s" % (ascii_letters, digits)
    cleaned_title = ''.join(c for c in title if c in valid_chars)
    return cleaned_title

def download_mp4():
    url = UIN.get("1.0", "end-1c")
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(download_path, exist_ok=True)
    cleaned_title = clean_video_title(yt.title)
    custom_filename = f"{cleaned_title}.mp4"
    file_path = os.path.join(download_path, custom_filename)
    stream.download(output_path=download_path, filename=custom_filename)
    print("MP4 downloaded successfully to:", file_path)

def download_mp3():
    url = UIN.get("1.0", "end-1c")
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(download_path, exist_ok=True)
    cleaned_title = clean_video_title(yt.title)
    custom_filename = f"{cleaned_title}.mp3"
    file_path = os.path.join(download_path, custom_filename)
    stream.download(output_path=download_path, filename=custom_filename)
    print("MP3 downloaded successfully to:", file_path)

window = tk.Tk()
window.geometry("500x300")
window.title("Youtube to MP4")
window.iconbitmap('Downloads\Dicon.ico')

window.configure(bg='#121212')

style = ttk.Style()
style.configure('TButton', foreground='#555555', background='#dcdcdc', font=('Helvetica', 12))
style.configure('TLabel', foreground='#ffffff', background='#121212', font=('Helvetica', 18))
style.configure('TFrame', background='#121212')

CP = ttk.Label(window, text="Copy and Paste Youtube Link Below")
CP.pack(padx=10, pady=20)

UIN = tk.Text(window, height=3, font=('Helvetica', 16), bg='#1e1e1e', fg='#ffffff')
UIN.pack(padx=10)

MP4 = ttk.Button(window, text="MP4", command=download_mp4, width=10)
MP4.pack(side=tk.LEFT, padx=60, pady=10)

MP3 = ttk.Button(window, text="MP3", command=download_mp3, width=10)
MP3.pack(side=tk.RIGHT, padx=60, pady=10)

window.mainloop()
