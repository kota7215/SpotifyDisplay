import os
import time
import tkinter as tk
from io import BytesIO

import requests
import spotipy
from PIL import Image, ImageTk
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
redirect = "https://localhost:8888/callback"
scope = "user-read-playback-state user-read-currently-playing"

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope, open_browser=True)
sp = spotipy.Spotify(auth_manager=sp_oauth)

previous_image_url = None
remaining_time = 5


def fetch_album_cover_url():
    global remaining_time
    try:
        # 現在の再生状態を取得
        current_playback = sp.current_playback()
        if current_playback and current_playback["is_playing"]:
            track = current_playback["item"]
            album_cover_url = track["album"]["images"][0]["url"]
            progress_ms = current_playback["progress_ms"]
            duration_ms = track["duration_ms"]
            remaining_time = (duration_ms - progress_ms) / 1000
            return album_cover_url
        else:
            return None
    except Exception as e:
        print(f"Error retrieving album cover URL: {e}")
        return None


def update_image_label(image_url, image_label):
    global previous_image_url
    if image_url != previous_image_url:
        response = requests.get(image_url)
        img_data = BytesIO(response.content)
        min_length = min(root.winfo_screenwidth(), root.winfo_screenheight())
        img = Image.open(img_data)
        img = img.resize((min_length, min_length), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        image_label.config(image=tk_img)
        image_label.image = tk_img
        previous_image_url = image_url


def main_loop():
    global root, remaining_time
    while True:
        album_cover_url = fetch_album_cover_url()
        if album_cover_url:
            update_image_label(album_cover_url, image_label)
        time.sleep(min(5, remaining_time))  # 基本は5秒ごとに画像をチェック


# Tkinterウィンドウの設定
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")  # 背景色を黒に設定
image_label = tk.Label(root, bg="black")
image_label.pack(fill=tk.BOTH, expand=True)

# メインループをバックグラウンドスレッドで実行
import threading

threading.Thread(target=main_loop, daemon=True).start()

root.mainloop()
