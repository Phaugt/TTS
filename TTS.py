import pygame, io
from gtts import gTTS

def doTTS(TTS):
    """save the TTS to ram"""
    with io.BytesIO() as file:
        gTTS(text=TTS, lang="en").write_to_fp(file)
        file.seek(0)
        #play the sound with pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == '__main__':
    print("Write TTS:")
    TTS = input(" >> ")
    doTTS(TTS)