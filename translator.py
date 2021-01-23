import speech_recognition as sr 
from googletrans import Translator 
from gtts import gTTS 
import os 
import pyaudio
import pyttsx3
from playsound import playsound    
  
# Creating Recogniser() class object 
r = sr.Recognizer() 
def SpeakText(command): 
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()
c=1 
s={'african':'af','arabic':'ar','bengali':'bs','chinese':'zh-cn','hebrew':'he','russian':'ru','punjabi':'pa','tamil':'ta','telugu':'te','malayalam':'ml','french':'fr'}
print("Select language for translation:\n")
for i in s:
  print("{}. {}".format(c,i))
  c+=1
c=0
while(1):
 try:
  with sr.Microphone() as source2:
    SpeakText("translation language")
    r.adjust_for_ambient_noise(source2, duration=0.2) 
    audio2 = r.listen(source2) 
    MyText = r.recognize_google(audio2) 
    MyText = MyText.lower() 
    if(MyText in s):
      to_lang=s[MyText]
      os.system("cls")
      print("English ---> {} translator".format(MyText)) 
      break 
 except sr.UnknownValueError: 
    print("Invalid") 

while(1):
 translator = Translator() 
 try:
  with sr.Microphone() as source2:
    SpeakText("Say text to translate")
    r.adjust_for_ambient_noise(source2, duration=0.2) 
    audio2 = r.listen(source2) 
    MyText = r.recognize_google(audio2) 
    MyText = MyText.lower() 
    if(MyText=="exit translator"):
      break   
    from_lang = 'en' 
    print("Phase to be Translated :"+ MyText) 
    text_to_translate = translator.translate(MyText,src= from_lang,dest= to_lang) 
    text = text_to_translate.text  
    speak = gTTS(text=text, lang=to_lang, slow= False)       
    speak.save("capture{}.mp3".format(c))
    c=c+1
    playsound("capture{}.mp3".format(c-1))
    os.system("del capture{}.mp3".format(c-1)) 
    
 except sr.UnknownValueError: 
    print("Invalid") 
     
