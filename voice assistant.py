
import pyttsx3    ##text to speech converter
import speech_recognition as sr   ## voice to text converter
import webbrowser   ## additional module-1. for web browser searching
import datetime ## additional module-2. for runtime time and date
import pyjokes  ## additional module3. for jokes

## func for speech_recognition
## takes speech and gives output as text
def speech_to_text():
    ## calling class
    recognizer=sr.Recognizer() ## Recognizer class-> catch voice through microphone
    ## ab microphone ke through age ka kam krge
    with sr.Microphone() as source:
        ## first hmne instruction milna chahiye ki kb bolna hain..
        ## microphone start hone ki instruction .
        print("Listening your Voice")
        print("Please Speak Something")
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
    obj1.setProperty('voice',voices[1].id)
    ## male voice ki speed ko km krna hain..
    rate=obj1.getProperty('rate')  ## runtime pr speech ki speed ko km/jada krwa skte hain.
    obj1.setProperty('rate',150)
    obj1.say(y)
    obj1.runAndWait()


if __name__ == '__main__':
    ## work only if we call jarvis else not work,no response
 
  if speech_to_text().lower() == "jarvis":
        data=speech_to_text().lower()
        if "your name" in data:
            name="my name is jarvis"
            text_to_speech(name)
        elif "old are you" in data:
            name ="Im just 1 year old"
            text_to_speech(name)
        elif "time" in data:
            time=datetime.datetime.now().strftime("%I%M%p")  ##I-> Hours,M-> Minute ,p-> a.m or p.m
            time1=datetime.datetime.now().date
            text_to_speech(time1)
            text_to_speech(time)
        elif "youtube" in data:
             webbrowser.open("https://www.youtube.com/")




   # else:
    #    print("Thanks ..")









