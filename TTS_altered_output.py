import pyttsx3

#init the TTS
TTS = pyttsx3.init()
TTS.setProperty('rate', 150)

#alter the voice output
voices = TTS.getProperty('voices')       #get info about the voices
#TTS.setProperty('voice', voices[0].id)  # 0 for male
#TTS.setProperty('voice', voices[1].id)   # 1 for female

#string to speak
#text = "pythonexplainedto.me"
#TTS.save_to_file(text,"male_"+text+".mp3")

#run the TTS
#TTS.runAndWait()
