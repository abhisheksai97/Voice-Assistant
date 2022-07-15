
import pyttsx3    ##text to speech converter
import speech_recognition as sr   ## voice to text converter
import webbrowser   ## additional module-1. for web browser searching
import datetime ## additional module-2. for runtime time and date
import pyjokes  ## additional module3. for jokes
import os
import time 
import  pywhatkit as py ## for whatsapp mssg sending
import smtplib as mail
import wikipedia as wiki



## func for speech_recognition
## takes speech and gives output as text
def speech_to_text():
    ## calling class

    recognizer=sr.Recognizer() ## Recognizer class-> catch voice through microphone
    ## ab microphone ke through age ka kam krge
    with sr.Microphone() as source:
        ## first hmne instruction milna chahiye ki kb bolna hain..
        ## microphone start hone ki instruction .
        print("Listening your Voice...")
        ##ab voice ke sath noice bhi aa skti hain,to noice ko hta do
        recognizer.adjust_for_ambient_noise(source)
        ## ab microphone listen krega , yha tk hmne pura sunn liya through microhone.
        audio=recognizer.listen(source)
        ## age bola to record hokr text me mill jayee, or ar bola hi nhi to error nhi dena chahiye
        ## so exception handling use kro
        try:
            print("Recognizing Now...")
            ## ab data ke name se voice ko store krwa lo 
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError as e:
             print("Not Understood ..")
             print("Kindly try Again")




def text_to_speech(y):
    ## call  class
    obj1=pyttsx3.init() ## init() -> init is class here.
    ## 2 different voice available here..
    ## 1-> of male 2 ->> of female
    voices =obj1.getProperty('voices')
    ##voices[0]-> for male voice , voices[1]-> for female voice.
    obj1.setProperty('voice',voices[0].id)
    ## male voice ki speed ko km krna hain..
    rate=obj1.getProperty('rate')  ## runtime pr speech ki speed ko km/jada krwa skte hain.
    obj1.setProperty('rate',120)
    obj1.say(y)
    obj1.runAndWait()

if __name__ == '__main__':
  text_to_speech("GoodMorning Sir")
  text_to_speech("Welcom To Voice Assistant  Abhishek")
  text_to_speech("How May i help you")
 ## work only if we call jarvis else not work,no response
  if  "javed" in speech_to_text().lower():
            while (True):
                    data=speech_to_text().lower()
                    if "your name" in data:
                     name="my name is jarvis"
                     text_to_speech(name)
                    elif "old are you" in data:
                          name ="Im just 1 year old"
                          text_to_speech(name)
                    elif "time" in data:
                       time=datetime.datetime.now().strftime("%I%M%p")  ##I-> Hours,M-> Minute ,p-> a.m or p.m
                       text_to_speech(time)
                    elif "date" in data:
                       time1=datetime.datetime.now().date
                       text_to_speech(time1)
                    elif "youtube" in data:
                         webbrowser.open("https://www.youtube.com/")
                    elif "practice" in data:
                      webbrowser.open("https://practice.geeksforgeeks.org")
                    elif " funny jokes" in data:
                      jokes1=pyjokes.get_joke(language="en",category="neutral")
                      print(jokes1)
                      speech_to_text(jokes1)
                    elif "wikipedia" in data:
                      summry=wiki.search('Obama')
                      text_to_speech(summry)
                    elif "play the song" in data:
                      add= "D:\songs"
                      listdata=os.listdir(add)
                      print(listdata)
                      os.startfile(os.path.join(add,listdata[0]))
                    elif "play the movie" in data:
                      text_to_speech("Movie Phir hera pheri started now")
                       
                   # elif "send message" in data:
                    #  py.sendwhatmsg('+919852177284','welcome to python project',1,1)
                    elif "mail" in data:
                      ob=mail.SMTP('smtp.gmail.com',587)
                      ob.ehlo()
                      ob.starttls()
                      ob.login('abhisheksaini.s2mca21@bvicam.in','Aryansaini88@@')
                      subject='test python'
                      body='hey buddy '
                      msg="subject:{}\n\n{}".format(subject,body)
                      listadd=['rajputishika318@gmail.com']
                      ob.sendmail('abhisheksaini.s2mca21@bvicam.in',listadd,msg)
                      print("mail sending completed..")
                      ob.quit()
                    elif "exit now" in data:
                         text_to_speech("closhing voice assistant")
                         break
                    time.sleep(5)  ## run each after 10 seconds only..

  else: 
        print("Thanks")









