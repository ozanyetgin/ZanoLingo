import speech_recognition as sr

def recognize_speech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        speech_sonuc = r.recognize_google(audio, language="en-GB")
        #print("Google Speech Recognition thinks you said: " + speech_sonuc)
        return speech_sonuc
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
