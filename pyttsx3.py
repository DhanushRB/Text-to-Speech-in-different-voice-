# # from gtts import gTTS
# import tts_project
# import os

# def online_tts(text, lang='en'):
#     try:
#         print("[INFO] Using Online TTS (gTTS)...")
#         tts = gTTS(text=text, lang=lang, slow=False)
#         tts.save("output_online.mp3")
#         os.system("start output_online.mp3")  # Windows (use 'afplay' for Mac or 'xdg-open' for Linux)
#     except Exception as e:
#         print("[ERROR] Online TTS failed:", e)

# def offline_tts(text):
#     try:
#         print("[INFO] Using Offline TTS (pyttsx3)...")
#         engine = tts_project.init()
#         engine.setProperty('rate', 150)
#         engine.setProperty('volume', 1.0)
#         engine.say(text)
#         # engine.say("Hello Dhanush, offline TTS is working now.")

#         engine.runAndWait()
#     except Exception as e:
#         print("[ERROR] Offline TTS failed:", e)

# # --------- MAIN PROGRAM ---------
# if __name__ == "__main__":
#     text = input("Enter text to convert into speech: ")

#     mode = input("Choose mode (1=Online / 2=Offline): ")

#     if mode == '1':
#         online_tts(text)
#     elif mode == '2':
#         offline_tts(text)
#     else:
#         print("Invalid choice! Use 1 for Online or 2 for Offline.")


# from gtts import gTTS
import pyttsx3
import os

def gTTS(text, lang='en', slow=False):
    raise NotImplementedError

def online_tts(text, lang='en'):
    try:
        print("[INFO] Using Online TTS (gTTS)...")
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("output_online.mp3")
        os.system("start output_online.mp3")  # Windows (use 'afplay' for Mac or 'xdg-open' for Linux)
    except Exception as e:
        print("[ERROR] Online TTS failed:", e)

def offline_tts(text, voice_type='male'):
    try:
        print(f"[INFO] Using Offline TTS (pyttsx3) with {voice_type} Indian voice...")
        engine = pyttsx3.init() # type: ignore

        # Set rate & volume
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)

        # Select Indian English voice
        voices = engine.getProperty('voices')
        selected_voice = None
        for v in voices:
            if "Indian" in v.name or "en-in" in v.id:
                if voice_type == 'male' and 'male' in v.name.lower():
                    selected_voice = v.id
                    break
                elif voice_type == 'female' and 'female' in v.name.lower():
                    selected_voice = v.id
                    break
        
        # If no gender match, fallback to any Indian English voice
        if not selected_voice:
            for v in voices:
                if "Indian" in v.name or "en-in" in v.id:
                    selected_voice = v.id
                    break
        
        if selected_voice:
            engine.setProperty('voice', selected_voice)

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("[ERROR] Offline TTS failed:", e)

# --------- MAIN PROGRAM ---------
if __name__ == "__main__":
    text = input("Enter text to convert into speech: ")
    mode = input("Choose mode (1=Online / 2=Offline): ")

    if mode == '1':
        online_tts(text)
    elif mode == '2':
        gender = input("Choose voice type (male/female): ")
        offline_tts(text, gender.lower())
    else:
        print("Invalid choice! Use 1 for Online or 2 for Offline.")
