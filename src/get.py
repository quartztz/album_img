import sys
from time import sleep
import requests
import spotipy
import spotipy.util as util

import os
import json

# from rich import print

USERNAME = "quartztz"
PATH_TO_IMAGE = "/home/quartztz/code/rs/album_img/assets/album_img.png"

def get_and_write_to_file(song): 
  # print(song)
  print("new song!")
  loc_url = song['item']['album']['images'][0]['url']
  url = loc_url

  image = requests.get(url)

  # os.remove(PATH_TO_IMAGE)

  file = open(PATH_TO_IMAGE, "wb")
  file.write(image.content)
  file.close()

def main(): 
  scope = 'user-read-currently-playing'

  token = util.prompt_for_user_token(USERNAME, scope, redirect_uri="http://127.0.0.1:8888/callback")
  old = None
  
  if token: 
    spotify = spotipy.Spotify(auth=token)
    # print("running properly! listening to your music")
    while True: 
      current = spotify.currently_playing()
        
      if old == None or current["item"]["album"]["name"] != old["item"]["album"]["name"]:
        old = current
        get_and_write_to_file(current)
      sleep(2)
    
  else: 
    print("invalid token")
    sys.exit()

if __name__ == "__main__": 
  main()
