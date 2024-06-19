from requests import get
from bs4 import BeautifulSoup 
import pyttsx3  
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
file = get("https://news.google.com/showcase?hl=en-IN&gl=IN&ceid=IN%3Aen")
r=file.text
soup = BeautifulSoup(r,'html.parser')
t=soup.findAll('a',{'class':'kEAYTc r5Cqre'})
s=0
SpeakText("Today's Headlines")
while(s!=15):
  print((s+1),t[s].text)
  SpeakText(t[s])
  s=s+1
