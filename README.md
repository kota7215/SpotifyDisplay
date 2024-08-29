# SpotifyDisplay
## Description
- Spotify Web APIを用いて，再生中のSpotifyの曲情報を取得し，表示するプログラム

## Usage
[Spotify for Developers Dashboard](https://developer.spotify.com/dashboard)にアクセスして，適当な名前でアプリを作成する。リダイレクトURLも適当で良く，`https://localhost:8888/callback`とかにしておく。作成できたらアプリの個別ページから設定を開いて，"Client ID"と"Client secret"をコピーして，環境変数への設定を`.zprofile`, `.bash_profile`にでも追加
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```

あとは`python main.py`を実行すればよい。初回だけSpotifyの認証画面が開くので，ログインすると適当なURLにリダイレクトされる。ブラウザのURL欄からURLをコピーしてきて，標準入力に貼り付ける。
