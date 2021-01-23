from requests import get
from bs4 import BeautifulSoup 
import pyttsx3  
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
file = get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en") 
r=file.text
soup = BeautifulSoup(r,'html.parser')
t=soup.findAll('a',{'class':'DY5T1d'})
s=0
SpeakText("Today's Headlines")
while(s!=len(t)):
  print((s+1),t[s].text)
  SpeakText(t[s])
  s=s+1
