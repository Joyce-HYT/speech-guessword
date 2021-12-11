import speech_recognition as sr

r = sr.Recognizer()
audiofile = sr.AudioFile('harvard.wav')

'''Audio file must be opened before record()'''
with audiofile as source:
    audio = r.record(source, duration=4) # 1-4sec file content
    audio2 = r.record(source, duration=4) # 5-8sec file content
    # audio = r.record(source) # whole file content

print(r.recognize_google(audio))
print(r.recognize_google(audio2))
