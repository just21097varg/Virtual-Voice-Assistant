import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import os
import youtube_dl
import urllib
import shutil
import moviepy.editor as mp 
from playsound import playsound 
import multiprocessing
import speech_recognition as sr 
import pyttsx3  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()
     

while(1):
   try:
       with sr.Microphone() as source2:
        SpeakText("Song name to play")
        r.adjust_for_ambient_noise(source2, duration=0.2) 
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        #MyText=input()
        MyText = MyText.lower() 
        music_name = MyText
        if music_name=="exit":
          SpeakText("Thanks for using music player")
          break
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        i=1
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[i]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[i])
        #ydl_opts = {'outtmpl': 'songs/{}.%(ext)s'.format(music_name)}
        #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #  ydl.download(['{}'.format(clip2)])
        music_name=music_name.replace(" ","_")
        os.system("youtube-dl --quiet --output songs/{}.mp4 {}".format(music_name,clip2))
        clip1 = mp.VideoFileClip(r"songs/{}.mp4".format(music_name),verbose=False) 
        clip1.audio.write_audiofile(r"audio/{}.mp3".format(music_name),verbose=False,logger=None)
        os.system("taskkill>NUL /F /IM ffmpeg-win64-v4.2.2.exe")
        os.system("del songs\{}.mp4".format(music_name))
        n="audio/{}.mp3".format(music_name)
        os.system("cls")
        os.system("echo Now Playing {}.......".format(music_name))
        playsound(n)
   except sr.UnknownValueError: 
      SpeakText("Sorry!! cannot recognize . Please try again") 