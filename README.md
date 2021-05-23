# tts-twitchbot
 Talking Twitch Chatbot

 This bot uses twitchio.ext to interact with a Twitch channel and pyttsx3 to speak text on your local computer. 

 If you are a streamer you can incorporate speech chatroom commands into your streams by capturing your PC's Desktop audio output. 

# Environment Preparation
##1) Install python3

##2) Install pyttsx3 Python Text To Speech library

https://pypi.org/project/pyttsx3/

Test it:
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

##3) Get TwitchIO installed and configured

https://twitchio.readthedocs.io/en/latest/index.html

# Configuration

## Obtain an oauth code
This code logs you into the chat server. 
https://twitchapps.com/tmi/

## Register your app with Twitch dev and request a client-id (so you can interface with Twitch's API)
