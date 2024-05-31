from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR UNIQUE CLIENT ID,
        client_secret=YOUR UNIQUE CLIENT SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=YOUR SPOTIFY DISPLAY NAME,
    )
)
user_id = sp.current_user()["id"]

# answer = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/2000-08-12/"

# clientid = "ab8c5cae0f604fe6bf65e6dc63f05170"
# clientsecret = "f68ba9707066412c9553f9ae08ba1646"

response = requests.get(url)
site = response.text

soup = BeautifulSoup(site,"html.parser")
top_songs_list = soup.select(selector='li ul li .c-title')
top_songs = [song.getText().strip() for song in top_songs_list]

