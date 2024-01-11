import speech_recognition as sr
r1 = sr.Recognizer()
mic = sr.Microphone()

print('Hey! You can speak now')
print('Tell me How is your day?')
with mic as source:
        audio = r1.listen(source)
        print('Thank You! for Speaking')
        print('This is your text')
        print(r1.recognize_google(audio))