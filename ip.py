import pyttsx3   
import socket
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
SpeakText("Your Computer Name is {}".format(hostname))    
SpeakText("Your Computer IP Address is {}".format(IPAddr))