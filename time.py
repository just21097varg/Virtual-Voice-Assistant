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
x = datetime.datetime.now()
SpeakText("Today's date is {}  {} {}".format(x.day,x.strftime("%B"),x.year))
SpeakText("And time is {}".format(x.strftime("%H:%M:%S")))
print("Current Date and time is {}".format(x))