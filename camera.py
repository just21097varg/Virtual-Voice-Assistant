import cv2
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


#function to capture image
def cap():
 count = 0

 while(True):

  try: 
   with sr.Microphone() as source2:
     r.adjust_for_ambient_noise(source2, duration=0.05) 
     audio2 = r.listen(source2) 
     MyText = r.recognize_google(audio2) 
     MyText = MyText.lower()  
     if(MyText=="capture"): 
       vid_cam = cv2.VideoCapture(0)

       SpeakText("Going to capture !! Give a pose!!")
       for i in range(50):
         if(i==40):
           SpeakText("Smile Please!!")
         _, image_frame = vid_cam.read()
        
         cv2.imshow('frame', image_frame)
 
         if cv2.waitKey(100) & 0xFF == ord('q'):
        
            break
 
       img_name = "images/opencv_frame_{}.png".format(count)
       cv2.imwrite(img_name, image_frame)
       print("{} written!".format(img_name))
       count+=1  
       vid_cam.release()

       cv2.destroyAllWindows()

     if(MyText=="exit"):
        SpeakText("Thanks for using camera!!")
        break
  
  except sr.UnknownValueError: 
    print("",end='')
 return count          
print("Give following commands :\n1. Capture\n2. Exit")
img_counter=cap()
if(img_counter==0):
    SpeakText("No image captured")
else:
    SpeakText("{} Image captured successfully".format(img_counter))