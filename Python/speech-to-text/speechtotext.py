import speech_recognition as sr

ss=sr.Recognizer()

with sr.Microphone() as source:
    print("speak anything")
    audio=ss.listen(source)
    try:
        text=ss.recognize_google(audio)
        print(text)
    except Exception as e:
        print("sorry couldn't hear you!")


