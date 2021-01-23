# Python program to translate 
# speech to text and text to speech 
import datetime   
import time  
import speech_recognition as sr 
import pyttsx3  
import os
import subprocess
from geopy.geocoders import Nominatim
import geocoder  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      

      
# Loop infinitely for user to 
# speak 
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
        print("Say 'Ok Virtual Assistant'")
        with sr.Microphone() as source: 
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source, duration=0.4) 
 
            #listens for the user's input  
            audio2 = r.listen(source) 
              
            # Using google to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            
            if(MyText=="ok virtual assistant"):
               SpeakText("Hello I'm your virtual assistant !! You can give me following commands to makes things easier!!") 
               os.system('cls')
               print("Use the following commands to instruct your virtual assistant:\n1. open youtube\n2. capture image\n3. play music\n4. time\n5. calculate\n6. my ip\n7. visual\n8. location\n9. game\n10. dictionary\n11. weather\n12. latest news\n13. language translator\n14. wikipedia\n15. close")
               
               while(1):
                os.system('cls')
                print("Use the following commands to instruct your virtual assistant:\n1. open youtube\n2. capture image\n3. play music\n4. time\n5. calculate\n6. my ip\n7. visual\n8. location\n9. game\n10. dictionary\n11. weather\n12. latest news\n13. language translator\n14. wikipedia\n15. close")
                with sr.Microphone() as source2:
                 try: 
                  r.adjust_for_ambient_noise(source2, duration=0.2) 
                  audio2 = r.listen(source2) 
                  MyText = r.recognize_google(audio2) 
                  MyText = MyText.lower() 
                  if(MyText=="dictionary"):
                    SpeakText("opening dictionary") 
                    os.system("py dictionary.py");
                  if(MyText=="game"):
                    SpeakText("Starting TicTacToe game")
                    os.system("start file:///C:/Users/JUSTIN/Desktop/MyProject/tictactoe.html") 
                  if(MyText=="location"):
                    g = geocoder.ip('me')
                    geolocator = Nominatim(user_agent="my_application")
                    location = geolocator.reverse("{},{}".format(g.lat,g.lng))
                    location=str(location)
                    l=location.split(', ')
                    print("Your Location is {} {}".format(l[-3],l[-1]))
                    SpeakText("Your Location is {} {}".format(l[-3],l[-1]))
                  if(MyText=="latest news"):
                    SpeakText("opening news app")
                    os.system("cls")
                    os.system("py news.py")
                  if(MyText=="wikipedia"):
                    SpeakText("opening wikipedia")
                    os.system("cls")
                    os.system("py wiki.py")
                  if(MyText=="language translator"):
                    SpeakText("opening translator app")
                    os.system("cls")
                    os.system("py translator.py")  
                  if(MyText=="weather"):
                    SpeakText("opening weather app say exit to close weather app")
                    os.system("py weather.py")
                    SpeakText("thanks for using weather app")  
                  if(MyText=="visual"):
                    SpeakText("Opening Path Finding Visualizer")
                    os.system("start file:///C:/xampp/htdocs/PathfindingVisualizer/index.html")
                  if(MyText=="my ip"):
                    os.system("py ip.py") 
                  if(MyText=="time"):
                    os.system("py time.py")
                  if(MyText=="close"):
                    os.system('cls') 
                    os.system("py close.py")
                    break
                  if(MyText=="open youtube"):
                    os.system('start www.youtube.com')
                  if(MyText=="calculate"):
                    SpeakText("opening calculator")  
                    os.system('cls') 
                    os.system("py calculator.py")
                  if(MyText=="play music"):
                    SpeakText("opening music player")
                    os.system('cls') 
                    os.system("py musicplayer.py")
                  if(MyText=="capture image"):
                   SpeakText("opening camera ..... Please wait!!")
                   os.system("cls")
                   os.system("py camera.py")
                 except sr.UnknownValueError: 
                   SpeakText("Sorry didn't understand what you said!!") 
    except sr.UnknownValueError: 
       SpeakText("Sorry didn't understand what you said!!") 