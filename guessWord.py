import time
import random
import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating API request
    "error":   `None` if no error occured or API could not be reached or
               speech was unrecognizable
    "recordContentn": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the ambient noise and record audio from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "recordContent": None
    }

    try:
        response["recordContent"] = recognizer.recognize_google(audio, language='cmn-Hant-TW')
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["水災", "火災", "小偷", "危險", "搶錢", "車禍"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    word = random.choice(WORDS)

    # show instructions and wait 3 seconds before starting the game
    instructions = (
        "從下列的詞彙中，猜猜看我在想什麼嘻嘻:\n"
        "{words}\n"
        "你有 {n} 次機會\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        # listen, if a recordContent is returned or API request failed, break
        for j in range(PROMPT_LIMIT):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["recordContent"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        # if there was an error, stop the game
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
            break

        # show the user the recordContent
        print("You said: {}".format(guess["recordContent"]))

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["recordContent"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        if guess_is_correct:
            print("Correct! You win!".format(word))
            break
        elif user_has_more_attempts:
            print("Incorrect. Try again.\n")
        else:
            print("Sorry, you lose!\n答案是 '{}'.".format(word))
            break
