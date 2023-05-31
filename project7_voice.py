from gtts import gTTS
import os
def text_to_audio(text, filename):
    tts=gTTS(text=text,lang='en')
    tts.save(filename)
    os.system(f"start{filename}")
text="Hello there, how are you?"
filename="audio.mp3"
text_to_audio(text, filename)
