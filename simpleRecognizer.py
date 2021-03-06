import speech_recognition as sr

'''Create instance'''
r = sr.Recognizer()
mic = sr.Microphone()
# clearfile = sr.AudioFile('harvard.wav')
# noisefile = sr.AudioFile('jackhammer.wav') # the stale smell of old beer lingers
#
# '''Audio file must be opened before record()'''
# with clearfile as source:
#     # audio = r.record(source) # whole file content
#     audio1 = r.record(source, duration=4) # 1-4sec file content
#     audio2 = r.record(source, duration=4) # 5-8sec file content
#     audio3 = r.record(source, offset=3, duration=4) # after 3sec then record 4sec file content
#
# '''Deal noise'''
# with noisefile as source:
#     r.adjust_for_ambient_noise(source, duration=0.5)
#     audio = r.record(source)
#
# print(r.recognize_google(audio))
# print(r.recognize_google(audio, show_all=True)) # show all possible recognition

'''Capture Microphone Input'''
try:
    with mic as source:
        audio = r.listen(source)
    print(r.recognize_google(audio, language='cmn-Hant-TW'))
except:
    print("Cannot recognize anything.")
