import pyttsx3

#init pyttsx3
TTS = pyttsx3.init()
voices = TTS.getProperty('voices')

#loop all the voices
for voice in voices:
    TTS.setProperty('voice', voice.id)
    TTS.say('pythonexplainedto.me')

TTS.runAndWait()