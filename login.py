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

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope, open_browser=False)
sp = spotipy.Spotify(auth_manager=sp_oauth)

current_playback = sp.current_playback()
