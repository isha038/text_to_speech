#import required module for text to speech
from gtts import gTTS
#import module to play the converted audio
import os
#text to converted to audio
my_text = "Welcome to Isha's world!"

#Language 
language = "en"

#passing the text and language to the engine & slow=False means it has high speed
obj = gTTS(text=my_text, lang=language, slow=False )

#Saving the converted audio into mp3 file
obj.save("speechfile.mp3")

#Playing the converted file
os.system("start speechfile.mp3")