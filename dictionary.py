import datetime   
import time  
import speech_recognition as sr 
import pyttsx3  
import os
import subprocess

r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
from PyDictionary import PyDictionary
SpeakText("opening dictionary ....... say exit to close dictionary")
dictionary=PyDictionary()
while(1):
   try:
     with sr.Microphone() as source2:
       SpeakText("Which word you want to know meaning?")
       r.adjust_for_ambient_noise(source2, duration=0.2) 
       audio2 = r.listen(source2)
       word = r.recognize_google(audio2) 
       if(word=="exit"):
         break 
       print(word)
       SpeakText(dictionary.meaning(word))
   except sr.UnknownValueError: 
       SpeakText("Sorry!! Invalid Command") 
SpeakText("Thanks for using dictionary")