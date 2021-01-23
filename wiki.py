import wikipedia
import pyttsx3 
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()
while(1):
  SpeakText("What you want to know about?")
  n=input()
  if(n=="exit"):
    SpeakText("thanks for using wikipedia")
    break
  s=wikipedia.summary("{}".format(n),sentences=3)
  print(s)
  SpeakText(s)