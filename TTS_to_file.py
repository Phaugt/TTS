import pyttsx3

#init the TTS
TTS = pyttsx3.init()
TTS.setProperty('rate', 150)

#string to speak
text = "pythonexplainedto.me"
TTS.save_to_file(text,text+".mp3")

#run the TTS
TTS.runAndWait()
