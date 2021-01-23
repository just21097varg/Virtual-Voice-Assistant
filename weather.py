from requests import get
import speech_recognition as sr 
import pyttsx3  
from bs4 import BeautifulSoup 
import re 
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()  
# to get data from website 
while(1):
 try:
   with sr.Microphone() as source2:
      SpeakText("Speak city name for which you want to know the temperature")
      r.adjust_for_ambient_noise(source2, duration=0.2) 
      audio2 = r.listen(source2)
      x = r.recognize_google(audio2) 
      x=x.lower() 
      if(x=="exit"):
        break
      file = get("https://www.google.com/search?q={}%20weather".format(x)) 
      r1=file.text
      soup = BeautifulSoup(r1,'html.parser')
      degree = u"\N{DEGREE SIGN}"
      s=re.compile("{}C".format(degree))
      t1=soup.find_all('a')
      t=soup.find_all(string=s)
      a=list(map(str,t1[16].text.split(' ')))
      if(len(t)==0):
        SpeakText("invalid input")
      elif(a[-1]=="weather"):
        l=t1[16].text[:-8]
        print("Did you mean {} ??\n{} temperature is {}".format(l,l,t[0]))
        SpeakText("Did you mean {} ??\n{} temperature is {}".format(l,l,t[0]))
      else:
        print("{} temperature is {}".format(x,t[0]))
        SpeakText("{} temperature is {}".format(x,t[0])) 
 except sr.UnknownValueError: 
   SpeakText("Sorry!! Invalid Command")

