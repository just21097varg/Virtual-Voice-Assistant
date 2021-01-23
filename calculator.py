import speech_recognition as sr 
import pyttsx3 
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
       SpeakText("First Number")
       r.adjust_for_ambient_noise(source2, duration=0.2) 
       audio2 = r.listen(source2)
       first = r.recognize_google(audio2) 
       if(first=="exit"):
         break
       print("First Number= {}".format(first))
       SpeakText("Second Number")
       r.adjust_for_ambient_noise(source2, duration=0.2) 
       audio2 = r.listen(source2)
       second = r.recognize_google(audio2)
       if(second=="exit"):
         break 
       print("Second Number= {}".format(second))
       SpeakText("Tell the operation to perform \n addition \n subtraction \n multiplication \n division")
       while(1):
         try:
           r.adjust_for_ambient_noise(source2, duration=0.2) 
           audio2 = r.listen(source2)
           operation = r.recognize_google(audio2) 
           if(operation=="addition"):
             print(int(first)+int(second))
             break
           elif(operation=="subtraction"):
             print(int(first)-int(second))
             break
           elif(operation=="multiplication"):
             print(int(first)*int(second))
             break
           elif(operation=="division"):
             print(int(first)/int(second)) 
             break
         except sr.UnknownValueError: 
            SpeakText("Sorry!! Invalid Command")  
   except sr.UnknownValueError: 
     SpeakText("Sorry!! Invalid Command") 