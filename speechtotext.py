import speech_recognition as srpi

# Initialize the recognizer
recognizer = srpi.Recognizer()

# Capture audio from the microphone
with srpi.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    # Use the recognizer to convert speech to text
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except srpi.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except srpi.RequestError as e:
    print("Could not request results; {0}".format(e))
