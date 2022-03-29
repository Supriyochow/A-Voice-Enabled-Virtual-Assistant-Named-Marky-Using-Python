import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
from pprint import pprint
from PyDictionary import PyDictionary

dictionary=PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)    
    if hour>=6 and hour<12:
        speak("Gooood Morning")
    elif hour>=12 and hour<18:
        speak("Gooood Afternoooon")
    elif hour>=18 and hour<22:
        speak("Gooood Evening")
    else:
        speak("Gooood Night, Hope your are not that tired")        

    speak("I am Marky Sir. How May I help you? ")        

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")   
        audio=r.listen(source)

    try:
        print("Recognising....")
        r.energy_threshold = 300
        r.pause_threshold = 1
        query = r.recognize_houndify(audio,'t-VUBl-JtE5_p6t8EmDlZg==','6pOMUxXLvSHQHCOkbIKczFdS1LMEnWs9-gLU6zUJeDK6plE7SCL9LcGYjbLrWUwSinWbie3l1BUrMu2dcoy2vw==') 
        print("You Said: {} \n".format(query))   
            

    except:
        #print(e)

        speak("Sorry I didn't understand")
        return "None"

    return query    


def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json();
def print_weather(result,city):
    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    speak("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    speak("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))    
    speak("Weather: {}".format(result['weather'][0]['main'])) 



if __name__=="__main__":
    #speak("Supriyo is a Good Boy:")
    wishMe()
    i=0
    while True:
    # if 1:
    
        query = takeCommand().lower()
        i=i+1
        # Logic for executing tasks based on query
        if i==1:

            if 'hey marky' in query:
                print("Marky: ",end=' ')
                print('Huuzoor, How may I help you')
                speak('Huuzoor, How may I help you')
        

            elif 'can you dance' in query:
                print("Marky: ",end=' ')  
                print("I'm a big fan of Madhuri Dixit's dance moves, I would love to learn dancing from her")
                speak("I'm a big fan of Madhuri Dixit's dance moves, I would love to learn dancing from her")

            elif 'dance' in query:
                print("Marky: ",end=' ')  
                print("I'm known to create wave-forms with my dance")
                speak("I'm known to create wave-forms with my dance")

            elif 'Which is your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")

            elif 'your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")    

            elif 'who was your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")

            elif 'first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ") 

            elif 'your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")        



            elif 'quest' in query:
                print("Marky: ",end=' ')
                print("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am your best friend")
                speak("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am your best friend")

            elif 'whats your gender' in query:
                print("Marky: ",end=' ') 
                print('I hope you are not that stupid. You can easily understand from my voice')    
                speak('I hope you are not that stupid. You can easily understand from my voice')

            elif 'do you ever get tired' in query:
                print("Marky: ",end=' ') 
                print("Rest is tiring if its not in your service")
                speak("Rest is tiring                   if its not               in your service")

            elif 'do you have feelings' in query:
                print("Marky: ",end=' ') 
                print("I might be inanimate. But I do have feelings. Loyalty and duty. And you can trust me without even batting an eyelid")
                speak("I might be inanimate. But I do have feelings.        Loyalty                 and             duty   .       And you can trust me without even batting an eyelid")    


            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, not now but i will learn it surely")
                speak("Nopes, not now but i will learn it surely")    

            elif 'sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, I,m not as smart as google")
                speak("Nopes, I,m not as smart as google")    

            elif 'open wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("According to wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)   

            elif 'please open wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("According to wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)     

            elif 'open microsoft word' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office word 2007 ....')
                speak('opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      


            elif 'please open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      
            
            elif 'can you open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      
    

            elif 'high marky' in query:
                print("Marky: ",end=' ') 
                print('Namaste, what can i do for you') 
                speak('Namaste, what can i do for you')         

            elif 'marky' in query:
                print("Marky: ",end=' ') 
                print('I am marky. I am here to help you. If this is not your answer please say that again by removing marky')  
                speak('I am marky. I am here to help you. If this is not your answer please say that again by removing marky') 


            elif 'open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office excel 2007 ....')
                speak('opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      


            elif 'please open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      
            
            elif 'can you open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')    

            elif 'meaning' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the meaning of ',last)
                speak('Telling the meaning of '+last)
                print("Marky: ",end=' ') 
                print(dictionary.meaning(last))
                speak(dictionary.meaning(last))


            elif 'synonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the synonym of ',last)
                speak('Telling the synonym of '+last)
                print("Marky: ",end=' ') 
                print(dictionary.synonym(last))
                speak(dictionary.synonym(last)) 


            elif 'antonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the antonym of ',last)
                speak('Telling the antonym of '+last)
                print("Marky: ",end=' ') 
                print(dictionary.antonym(last))
                speak(dictionary.antonym(last))        

            elif 'translate' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the translationof ',last)
                speak('Telling the translation of '+last)
                print("Marky: ",end=' ') 
                print(dictionary.translate(last,'ben'))
                speak(dictionary.translate(last,'ben')) 
                 

            elif 'who made yoo' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')

            elif 'who made you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')  

            elif 'who made yoo marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')      

            elif 'who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'marky who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'who is your creator marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ')   

            elif 'who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyything ')   
                
            elif 'marky who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everything ')   

            elif 'who designed you marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everything ')   
                    
            elif "temperature" in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ')
                try:
	                query='q='+last;
                    w_data=weather_data(query);
                    print_weather(w_data, last)
                    print()
                
                except:
	                print('City name not found...')

            elif 'by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')   

            elif 'marky by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'by whom you were created marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:') 

            elif 'who is Supreyo Chowdhury marky' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')    

            elif 'marky who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')     

            elif 'who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")

            elif 'marky who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Supreyo marky' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")

            elif 'marky who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")    

            elif 'who is Bunty marky' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the pet name of Supriyo. And he is my creator ")
                speak("Bunty is the pet name of Supriyo. And he is my creator ")    


            elif 'play music' in query:
                print("Marky: ",end=' ') 
                music_dir = 'E:\\Banti\\english songs'
                songs = os.listdir(music_dir)
                print('playing music...')
                speak("playing music...")     
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'play any music' in query:
                print("Marky: ",end=' ') 
                music_dir = 'E:\\Banti\\english songs'
                songs = os.listdir(music_dir)
                print('playing music...')
                speak("playing music...")     
                os.startfile(os.path.join(music_dir, songs[0])) 

            elif 'play my favourite english song' in query:
                print("Marky: ",end=' ')
                print('playing your favourite english song...')
                speak("playing your favourite english song")     
                os.startfile('E:\\Banti\\english songs\\Alan Walker - Faded (Lyrics Video).mp3')       



            elif 'open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")

            elif 'can you please open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")     

            elif 'marky open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")  

            elif 'please open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'can you open the google' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening google.....')
                speak('sure, why notopening google....')
                webbrowser.open("google.com")      

            elif 'open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")          

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")    

            elif 'can you open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")    

            elif 'bye' in query:
                print("Marky: ",end=' ') 
                print("Have a nice day sir. Happy to help you ")
                speak("Have a nice day sir. Happy to help you")
                exit()

        
    




            elif 'open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")

            elif 'can you please open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'marky open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")  

            elif 'please open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'can you open the youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening youtube.....')
                speak('sure, why notopening youtube....')
                webbrowser.open("youtube.com")      

            elif 'open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")          

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")    

            elif 'can you open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")

            elif 'whats the time marky' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time now' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}") 

            elif 'tell me the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")       






            elif 'please help me marky' in query:
                print("Marky: ",end=' ') 
                print('I am there to do that only. Tell me what can I do for you')      
                speak('I am there to do that only. Tell me what can I do for you')   

            elif 'i love you' in query:
                print("Marky: ",end=' ') 
                print('What a wonderful thing to say!')  
                speak('What a wonderful thing to say!')  

            elif 'i love you marky' in query:
                print("Marky: ",end=' ') 
                print('You Just made my day:')  
                speak('You Just made my day')    

           # elif 'who is your father':
               # print("Marky: ",end=' ')
               # print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
               # speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")    

            #elif 'whos your father':
               # print("Marky: ",end=' ')
              #  print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
              #  speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")      


            else:
                print("Marky: ",end=' ') 
                print('can you please say that again: ') 
                speak('can you please say that again: ')   

                


















































































        elif i==2:
            if 'hey marky' in query:
                print("Marky: ",end=' ') 
                print('Hi there, How may I help you')
                speak('Hi there, How may I help you')

            elif 'high marky' in query:
                print("Marky: ",end=' ') 
                print('Hello, what can i do for you')
                speak('Hello, what can i do for you')  

            elif 'whats your gender' in query:
                print('I hope you are not that stupid. You can easily understand from my voice')    
                speak('I hope you are not that stupid. You can easily understand from my voice')

            elif 'Which is your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")

            elif 'your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")    

            elif 'who was your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")

            elif 'first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ") 

            elif 'your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")    

     

            elif 'play music' in query:
                print("Marky: ",end=' ') 
                music_dir = 'E:\\Banti\\english songs'
                songs = os.listdir(music_dir)
                print('playing music...')
                speak("playing music...")     
                os.startfile(os.path.join(music_dir, songs[0]))  

            elif "temperature" in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ')
                try:
	                query='q='+last;
	                w_data=weather_data(query);
	                print_weather(w_data, last)
	                print()
                
                except:
	                print('City name not found...')    


            elif 'can you dance' in query:
                print("Marky: ",end=' ')   
                print("I am always dancing on the inside")
                speak("I am always dancing on the inside")

            elif 'dance' in query:
                print("Marky: ",end=' ')   
                print("I am a Disco Dancer")
                speak("I am a Disco Dancer")

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, not now but i will learn it surely")
                speak("Nopes, not now but i will learn it surely")    

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, I,m not as smart as google")
                speak("Nopes, I,m not as smart as google")    

            elif 'quest' in query:
                print("Marky: ",end=' ')
                print("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")
                speak("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")    

            elif 'do you have feelings' in query:
                print("Marky: ",end=' ') 
                print("I might be inanimate. But I do have feelings. Loyalty and duty. And you can trust me without even batting an eyelid")
                speak("I might be inanimate. But I do have feelings.                Loyalty                   and                             duty   . And you can trust me without even batting an eyelid")

            elif 'open microsoft word' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office word 2007 ....')
                speak('opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      


            elif 'please open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      
            
            elif 'can you open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')        


            elif 'open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office excel 2007 ....')
                speak('opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      


            elif 'please open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      
            
            elif 'can you open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007') 
     



            elif 'marky' in query:
                print("Marky: ",end=' ') 
                print('I am marky. I am here to help you. If this is not your answer please say that again by removing marky')  
                speak('I am marky. I am here to help you. If this is not your answer please say that again by removing marky') 

            elif 'meaning' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the meaning of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.meaning(last))
                speak(dictionary.meaning(last)) 

            elif 'synonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the synonym of ',last)
                speak('Telling the synonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.synonym(last))
                speak(dictionary.synonym(last))     

            elif 'antonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the antonym of ',last)
                speak('Telling the antonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.antonym(last))
                speak(dictionary.antonym(last))     


            elif 'who made yoo' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')

            elif 'who made you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')  

            elif 'who made yoo marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')      

            elif 'who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'marky who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'who is your creator marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ')   

            elif 'who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyything ')   
                
            elif 'marky who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyything ')   

            elif 'who designed you marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyyyything ')   
                    
                           

            elif 'by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')   

            elif 'marky by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'by whom you were created marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:') 

            elif 'bye' in query:
                print("Marky: ",end=' ') 
                print("Have a nice day sir. Happy to help you ")
                speak("Have a nice day sir. Happy to help you")
                exit()    

            elif 'who is Supreyo Chowdhury marky' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')    

            elif 'marky who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')     

            elif 'who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")

            elif 'marky who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Supreyo marky' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")

            elif 'marky who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")    

            elif 'who is Bunty marky' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the pet name of Supriyo. And he is my creator ")
                speak("Bunty is the pet name of Supriyo. And he is my creator ")  



            elif 'open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")

            elif 'can you please open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'marky open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")  

            elif 'please open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'can you open the youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening youtube.....')
                speak('sure, why notopening youtube....')
                webbrowser.open("youtube.com")      

            elif 'open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")          

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")    

            elif 'can you open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com") 


            elif 'the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")

            elif 'whats the time marky' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time now' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}") 

            elif 'tell me the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}") 

            elif 'do you ever get tired?' in query:
                print("Marky: ",end=' ') 
                print("Rest is tiring if its not in your service")
                speak("Rest is tiring if its not in your service")    


            
            
            elif 'open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")

            elif 'can you please open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")     

            elif 'marky open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")  

            elif 'please open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'can you open the google' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening google.....')
                speak('sure, why notopening google....')
                webbrowser.open("google.com")      

            elif 'open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")          

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")    

            elif 'can you open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")    








            elif 'please help me marky' in query:
                print("Marky: ",end=' ') 
                print('I am there to do that only. Tell me what can I do for you')      
                speak('I am there to do that only. Tell me what can I do for you')  

            elif 'i love you' in query:
                print("Marky: ",end=' ') 
                print('You love me? This is a wonderful day')  
                speak('You love me? This is a wonderful day')   

            elif 'i love you marky' in query:
                print("Marky: ",end=' ') 
                print('What a wonderful thing to say!')  
                speak('What a wonderful thing to say!') 

           # elif 'who is your father':
                #print("Marky: ",end=' ')
              #  print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
               # speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")    

           # elif 'who\'s your father':
               # print("Marky: ",end=' ')
               # print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
               # speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")      
            

            else:
                print("Marky: ",end=' ') 
                print('can you please say that again: ') 
                speak('can you please say that again: ')      

           







































































































































        elif i==3:
            
            if 'hey marky' in query:
                print("Marky: ",end=' ') 
                print('Hello, How may I help you')
                speak('Hello, How may I help you')

            elif 'high marky' in query:
                print("Marky: ",end=' ') 
                print('Hello Ji, what can i do for you')
                speak('Hello Ji, what can i do for you')  

            elif 'whats your gender' in query:
                print('I hope you are not that stupid. You can easily understand from my voice')    
                speak('I hope you are not that stupid. You can easily understand from my voice')    

            elif 'Which is your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")

            elif 'your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")   

            elif 'who was your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")

            elif 'first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ") 

            elif 'your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")     

            elif 'can you dance' in query:
                print("Marky: ",end=' ')   
                print("Maybe I am a better dancer than you")
                speak("Maybe I am a better dancer than you")

            elif 'dance' in query:
                print("Marky: ",end=' ')   
                print("Dancing is the best, someday, I'd love to be a part of the world's longest conga line")
                speak("Dancing is the best, someday, I'd love to be a part of the world's longest conga line")  

                      

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, not now but i will learn it surely")
                speak("Nopes, not now but i will learn it surely")    

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, I,m not as smart as google")
                speak("Nopes, I,m not as smart as google")


            elif 'open microsoft word' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office word 2007 ....')
                speak('opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      


            elif 'please open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      
            
            elif 'can you open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')        
            
            elif 'do you have feelings' in query:
                print("Marky: ",end=' ') 
                print("I might be inanimate. But I do have feelings. Loyalty and duty. And you can trust me without even batting an eyelid")
                speak("I might be inanimate. But I do have feelings.        Loyalty      and     duty   . And you can trust me without even batting an eyelid")

            elif "temperature" in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ')
                try:
	                query='q='+last;
	                w_data=weather_data(query);
	                print_weather(w_data, last)
	                print()
                
                except:
	                print('City name not found...')


            elif 'open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office excel 2007 ....')
                speak('opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      


            elif 'please open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      
            
            elif 'can you open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007') 

            elif 'meaning' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the meaning of ',last)
                speak('Telling the meaning of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.meaning(last))
                speak(dictionary.meaning(last)) 

            elif 'synonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the synonym of ',last)
                speak('Telling the synonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.synonym(last))
                speak(dictionary.synonym(last))

            elif 'antonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the antonym of ',last)
                speak('Telling the antonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.antonym(last))
                speak(dictionary.antonym(last))    

            elif 'quest' in query:
                print("Marky: ",end=' ')
                print("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")
                speak("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")    



            elif 'play music' in query:
                print("Marky: ",end=' ') 
                music_dir = 'E:\\Banti\\english songs'
                songs = os.listdir(music_dir)
                print('playing music...')
                speak("playing music...")     
                os.startfile(os.path.join(music_dir, songs[0]))    

            elif 'marky' in query:
                print("Marky: ",end=' ') 
                print('I am jarvis. I am here to help you. If this is not your answer please say that again by removing jarvis')  
                speak('I am jarvis. I am here to help you. If this is not your answer please say that again by removing jarvis') 


            elif 'who made yoo' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')

            elif 'who made you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')  

            elif 'who made yoo marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')      

            elif 'who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'marky who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'who is your creator marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ')   

            elif 'who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyything ')   
                
            elif 'marky who designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyything ')   

            elif 'who designed you marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everyyyyyything ')   
                    

            elif 'bye' in query:
                print("Marky: ",end=' ') 
                print("Have a nice day sir. Happy to help you ")
                speak("Have a nice day sir. Happy to help you")
                exit()        
                           

            elif 'by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')   

            elif 'marky by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'by whom you were created marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:') 

            elif 'who is Supreyo Chowdhury marky' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')    

            elif 'marky who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')     

            elif 'who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")

            elif 'marky who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Supreyo marky' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")

            elif 'marky who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")    

            elif 'who is Bunty marky' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the pet name of Supriyo. And he is my creator ")
                speak("Bunty is the pet name of Supriyo. And he is my creator ") 


            elif 'open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")

            elif 'can you please open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'marky open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")  

            elif 'please open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'can you open the youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening youtube.....')
                speak('sure, why notopening youtube....')
                webbrowser.open("youtube.com")      

            elif 'open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")          

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")    

            elif 'can you open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")

            elif 'whats the time marky' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time now' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}") 

            elif 'tell me the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")     




            elif 'open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")

            elif 'do you ever get tired?' in query:
                print("Marky: ",end=' ') 
                print("Rest is tiring if its not in your service")
                speak("Rest is tiring if its not in your service")    

            elif 'can you please open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")     

            elif 'marky open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")  

            elif 'please open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'can you open the google' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening google.....')
                speak('sure, why notopening google....')
                webbrowser.open("google.com")      

            elif 'open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")          

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")    

            elif 'can you open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")  




            elif 'please help me marky' in query:
                print("Marky: ",end=' ') 
                print('I am there to do that only. Tell me what can I do for you')      
                speak('I am there to do that only. Tell me what can I do for you')  

            elif 'i love you' in query:
                print("Marky: ",end=' ') 
                print('I cant measure how much I love you. But I can spend my entire life searching for you:')  
                speak('I cant measure how much I love you. But I can spend my entire life searching for you:') 

            elif 'i love you jarvis' in query:
                print("Marky: ",end=' ') 
                print('I cant measure how much I love you. But I can spend my entire life searching for you:')  
                speak('I cant measure how much I love you. But I can spend my entire life searching for you:')    



            #elif 'who is your father':
              #  print("Marky: ",end=' ')
              #  print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
               # speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")    

            #elif 'who\'s your father':
                #print("Marky: ",end=' ')
               # print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
              #  speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")             

            else:
                print("Marky: ",end=' ') 
                speak('Opps I didnt get that ')
                speak('Opps I didnt get that ')   

                     

























































































































































        elif i==4:
            if 'hey marky' in query:
                print("Marky: ",end=' ') 
                print('Dont bore me.., tell me How may I help you or')
                speak('Dont bore me.., tell me How may I help you or')

            elif 'high marky' in query:
                print("Marky: ",end=' ') 
                print('Stop kidding, and tell me how may i help you')
                speak('Stop kidding, and tell me how may i help you')  

            elif 'whats your gender' in query:
                print('I hope you are not that stupid. You can easily understand from my voice')    
                speak('I hope you are not that stupid. You can easily understand from my voice')    

            elif 'Which is your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")

            elif 'your favourite marvel Character' in query:
                print("Marky: ",end=' ')  
                print("Well my favourite Marvel character is the creator of Marvel Characters, Stan Lee ")
                speak("Well my favourite Marvel character is       the creator of Marvel Characters,              Stan Lee ")    

            elif 'who was your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")

            elif 'first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ") 

            elif 'your first crush' in query:
                print("Marky: ",end=' ')  
                print("My first crush is my creator. Ofcourse I fell in love with him when he started creating me ")
                speak("My first crush is my creator.             Ofcourse I fell in love with him when he started creating me ")    

            elif 'play music' in query:
                print("Marky: ",end=' ') 
                music_dir = 'E:\\Banti\\english songs'
                songs = os.listdir(music_dir)
                print('playing music...')
                speak("playing music...")     
                os.startfile(os.path.join(music_dir, songs[0])) 

            elif 'quest' in query:
                print("Marky: ",end=' ')
                print("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")
                speak("My quest is to make your life as comfortable as possible, so that you enjoy my services and feel free to express yourself to me. I am you best friend")       


                

            elif 'marky' in query:
                print("Marky: ",end=' ') 
                print('I am marky. I am here to help you. If this is not your answer please say that again by removing marky')  
                speak('I am marky. I am here to help you. If this is not your answer please say that again by removing marky') 


            elif 'open microsoft word' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office word 2007 ....')
                speak('opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      


            elif 'please open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')      
            
            elif 'can you open microsoft word' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office word 2007 ....')
                speak('sure, opening microsoft office word 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007')    
            
            elif 'open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('opening Microsoft office excel 2007 ....')
                speak('opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      


            elif 'please open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007')      
            
            elif 'can you open microsoft excel' in query:
                print("Marky: ",end=' ')
                print('sure, opening Microsoft office excel 2007 ....')
                speak('sure, opening microsoft office excel 2007 ....')
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007') 
            elif 'meaning' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the meaning of ',last)
                speak('Telling the meaning of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.meaning(last))
                speak(dictionary.meaning(last)) 

            elif "temperature" in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ')
                try:
	                query='q='+last;
	                w_data=weather_data(query);
	                print_weather(w_data, last)
	                print()
                
                except:
	                print('City name not found...')


            elif 'synonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the synonym of ',last)
                speak('Telling the synonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.synonym(last))
                speak(dictionary.synonym(last))

            elif 'antonym' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the antonym of ',last)
                speak('Telling the antonym of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.antonym(last))
                speak(dictionary.antonym(last))  

            elif 'translate' in query:
                word_list=query.split()
                last=word_list[-1] 
                print("Marky: ",end=' ') 
                print('Telling the translationof ',last)
                speak('Telling the translation of ',last)
                print("Marky: ",end=' ') 
                print(dictionary.translate(last,'ben'))
                speak(dictionary.translate(last,'ben'))      



            elif 'who made you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')


            elif 'can you dance' in query:
                print("Marky: ",end=' ')   
                print("Maybe I am a better dancer than you")
                speak("Maybe I am a better dancer than you")

            elif 'do you ever get tired?' in query:
                print("Marky: ",end=' ') 
                print("Rest is tiring if its not in your service")
                speak("Rest is tiring if its not in your service")    

            elif 'dance' in query:
                print("Marky: ",end=' ')   
                print("Dancing is the best, someday, I'd love to be a part of the world's longest conga line")
                speak("Dancing is the best, someday, I'd love to be a part of the world's longest conga line")   

            elif 'do you have feelings' in query:
                print("Marky: ",end=' ') 
                print("I might be inanimate. But I do have feelings. Loyalty and duty. And you can trust me without even batting an eyelid")
                speak("I might be inanimate. But I do have feelings.        Loyalty      and     duty   . And you can trust me without even batting an eyelid")    

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, not now but i will learn it surely")
                speak("Nopes, not now but i will learn it surely")    

            elif 'can you sing' in query:
                print("Marky: ",end=' ')  
                print("Nopes, I,m not as smart as google")
                speak("Nopes, I,m not as smart as google") 


            elif 'marky who made you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')  

            elif 'who made you marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. I just love him: ')
                speak('Well thats Supreyo Chowdhury. i just love him: ')      

            elif 'who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'marky who is your creator' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ') 

            elif 'who is your creator marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He is a genius ')
                speak('Well thats Supreyo Chowdhury. He is a genius ')   

            elif 'who is designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everything ')   
                
            elif 'marky who is designed you' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everything ')   

            elif 'who is designed you marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. He knows everything ')
                speak('Well thats Supreyo Chowdhury. He knows everything ')   
                    
                           

            elif 'by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')   

            elif 'marky by whom you were created' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'by whom you were created marky' in query:
                print("Marky: ",end=' ') 
                print('Well thats Supriyo Chowdhury. Nobody is like him ')
                speak('Well thats Supreyo Chowdhury. Nobody is like him ')    

            elif 'who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:') 

            elif 'who is Supreyo Chowdhury marky' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')    

            elif 'marky who is Supreyo Chowdhury' in query:
                print("Marky: ",end=' ') 
                print('Well he is my creator. So technically he is my father: ')
                speak('Well he is my creator. So technically he is my father:')     

            elif 'who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")

            elif 'marky who is Supreyo' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Supreyo marky' in query:
                print("Marky: ",end=' ') 
                print("He is a great man. Technically he is my father: ")
                speak("He is a great man. Technically he is my father: ")    

            elif 'who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")

            elif 'marky who is Bunty' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the nick name of Supriyo. And he is my creator ")
                speak("Bunty is the nick name of Supriyo. And he is my creator ")    

            elif 'who is Bunty marky' in query:
                print("Marky: ",end=' ') 
                print("Bunty is the pet name of Supriyo. And he is my creator ")
                speak("Bunty is the pet name of Supriyo. And he is my creator ")    


            elif 'bye' in query:
                print("Marky: ",end=' ') 
                print("Have a nice day sir. Happy to help you ")
                speak("Have a nice day sir. Happy to help you")
                exit()    



            elif 'open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")

            elif 'can you please open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'marky open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")  

            elif 'please open youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")   

            elif 'can you open the youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening youtube.....')
                speak('sure, why not opening youtube....')
                webbrowser.open("youtube.com")      

            elif 'open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")          

            elif 'please open the youtube' in query:
                print("Marky: ",end=' ') 
                print('opening youtube.....')
                speak('opening youtube....')
                webbrowser.open("youtube.com")    

            elif 'can you open youtube' in query:
                print("Marky: ",end=' ') 
                print('sure, opening youtube.....')
                speak('sure, opening youtube....')
                webbrowser.open("youtube.com")     

            elif 'open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")

            elif 'can you please open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")     

            elif 'marky open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")  

            elif 'please open google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")   

            elif 'can you open the google' in query:
                print("Marky: ",end=' ') 
                print('sure, why not, opening google.....')
                speak('sure, why notopening google....')
                webbrowser.open("google.com")      

            elif 'open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")          

            elif 'please open the google' in query:
                print("Marky: ",end=' ') 
                print('opening google.....')
                speak('opening google....')
                webbrowser.open("google.com")    

            elif 'can you open google' in query:
                print("Marky: ",end=' ') 
                print('sure, opening google.....')
                speak('sure, opening google....')
                webbrowser.open("google.com")  



            elif 'the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"the time is {strTime}")

            elif 'whats the time marky' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'whats the time now' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}") 

            elif 'tell me the time' in query:
                print("Marky: ",end=' ') 
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")      


            elif 'please help me marky' in query:
                print("Marky: ",end=' ') 
                print('I am there to do that only. Tell me what can I do for you')      
                speak('I am there to do that only. Tell me what can I do for you')


            elif 'i love you' in query:
                print("Marky: ",end=' ') 
                print('You love me? This is a wonderful day')  
                speak('You love me? This is a wonderful day')    

            elif 'i love you jarvis' in query:
                print("Marky: ",end=' ') 
                print('You love me? This is a wonderful day')  
                speak('You love me? This is a wonderful day')  

           # elif 'who is your father':
              #  print("Marky: ",end=' ')
              #  print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
           #     speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")    

            #elif 'who\'s your father':
              #  print("Marky: ",end=' ')
              #  print("I am an AI. I was created by Supriyo Chowdhury. So technically he is my father")
              # speak("I am an AI. I was created by Supreyo Chowdhury. So technically he is my father")           

            else:
                print("Marky: ",end=' ') 
                print(' Sorry I didnt get that')
                speak(' Sorry I didnt get that')   

                             

        elif i==5:
            i=0
        else:
            print("Marky: ",end=' ') 
            print('Can you please say that again: ')
            speak('Can you please say that again: ')                 
            
