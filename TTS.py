import pyttsx3

#init the TTS
TTS = pyttsx3.init()

#string to speak
TTS.say("pythonexplainedto.me")

#run the TTS
TTS.runAndWait()
