import speech_recognition as sr
def listen():
    cmd = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening..")
        cmd.pause_threshold = 0.8  # WAIT AFTER LISTENING
        cmd.energy_threshold = 100  # AMPLITUDE OF USER VOICE
        audio = cmd.listen(source, 0, 3)
    try:
        print("Recognizing...")
        query = cmd.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
    except Exception as e:
        print("Couldn't fetch Voice")
        return "None"
    return query
