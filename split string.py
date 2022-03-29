import speech_recognition as sr

def takeCommand():
   # It Takes Microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")   
        audio=r.listen(source)
        

    try:
        print("Recognising....")
        r.energy_threshold = 300
        r.pause_threshold = 1
        query = r.recognize_houndify(audio) 
        print("You Said: {} \n".format(query))   
        if query=='meaning':
            print()

    except:
        #print(e)

        print("Sorry I didn't understand")
        return "None"

    return query    

if __name__=="__main__":
    query= takeCommand().lower()
    if query=="meaning":

        text=input()
        word_list=text.split()
        print(word_list[-1])

    else:
        print("Please reenter")    