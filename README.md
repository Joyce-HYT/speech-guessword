# audio program
I tried to process audio from
[realpython](https://realpython.com/python-speech-recognition/)
sample code by David Amos.

## simpleRecognizer.py
This program is divided into 4 parts.
1. Create instance from speech_recognition library.
2. Open audio file.
3. Deal noises.
4. Capture microphone input.

Notice: some variable name are repeated, if you want to try this code, you need to comment somewhere.

## guessWord.py
This is Taiwanese version of the guess word game.

```python
# set the list of words, maxnumber of guesses, and prompt limit
WORDS = ["水災", "火災", "小偷", "危險", "搶錢", "車禍"]
NUM_GUESSES = 3
PROMPT_LIMIT = 5
```

You can change word list, guesses number and prompt limit.

```python
try:
    response["recordContent"] = recognizer.recognize_google(audio, language='cmn-Hant-TW')
```

In addition you can set the language of the recognizer.
