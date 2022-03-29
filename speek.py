import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio=r.listen(source)

    try:
        text=r.recognize_houndify(audio)
        print("You Said: {} ".format(text))
        speak(text)

    except:
        print("Please say it again:")    