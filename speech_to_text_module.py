import speech_recognition as sr

r = sr.Recognizer()


def get_text_from_speech():
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                text = r.recognize_google(audio2)
                text = text.lower()
                if text:
                    print("identified text is ", text)
                    return text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")


if __name__ == "__main__":
    resulting_text = get_text_from_speech()
    print(resulting_text)
