import datetime   
import time  
import pyttsx3
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
t = time.localtime()
ctime = time.strftime("%H", t)
if(int(ctime)>=19 or int(ctime)<=5):
   SpeakText("Thanks!! for using virtual assistant. Have a nice bedtime. Good night")
else:
   SpeakText("Thanks!! for using virtual assistant. Have a nice day ahead!")