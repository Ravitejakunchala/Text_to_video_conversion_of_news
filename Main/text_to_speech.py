from gtts import gTTS
import os
import pyttsx3
def text_to_speech(text,name):
    # mytext = text
    # # Language in which you want to convert
    # language = 'en'
    # te= 'co.in'
    #
    # myobj = gTTS(text= mytext, lang=language, tld=te ,slow=False)
    #
    # filename=name+'.mp3'
    # myobj.save(filename)
    #
    # # os.system(filename)
    # return filename


    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')  # get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    engine.setProperty('voice', voice[0].id)
    engine.setProperty('volume', 1.0)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    tex = text
    tex = tex.replace(". ", " ")
    #
    # # print(tex)
    filename=name+'.mp3'
    engine.save_to_file(tex, filename)
    engine.runAndWait()
    return filename
    # say method on the engine that passing input text to be spoken
    # engine.say(tex)

    # run and wait method, it processes the voice commands.
    # engine.runAndWait()

# text_to_speech("vbnm","fgcvhbjnk")