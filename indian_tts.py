# from gtts import gTTS
# import tempfile
# import os
# import platform

# # Function to play the audio file
# def play_audio(path):
#     if platform.system() == "Windows":
#         os.system(f'start "" "{path}"')  # start requires "" before the path
#     elif platform.system() == "Darwin":  # macOS
#         os.system(f'afplay "{path}"')
#     else:  # Linux
#         os.system(f'mpg123 "{path}"')

# print("🎙️ Indian English TTS (no file saved) — type 'exit' to quit")

# while True:
#     text = input("\n📝 Enter text: ")
#     if text.lower() == 'exit':
#         print("👋 Exiting.")
#         break

#     # Generate TTS with Indian accent
#     tts = gTTS(text=text, lang='en', tld='co.in')  # 'co.in' = Indian accent

#     # Save to a temporary mp3 file (close before using it)
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#         temp_path = fp.name  # Save path before closing
#     tts.save(temp_path)  # Save after file is closed

#     print("🔊 Speaking...")
#     play_audio(temp_path)

#     # Optional: Delete after playback
#     # os.remove(temp_path)



import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Change voice properties
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Text input
text = "Hi Dhanush, this is your offline text to speech system."

# Convert text to speech
engine.say(text)
engine.runAndWait()
