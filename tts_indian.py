# from TTS.api import TTS
# import os

# # Load a multi-speaker, multilingual model
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

# # Input text
# text = "Hello Dhanush, this is an offline Indian English text to speech system."

# # Generate speech
# tts.tts_to_file(text=text, file_path="output.wav")

# # Play output
# os.system("start output.wav")  # Windows
import asyncio
import edge_tts
import os

async def text_to_speech(text, voice="en-IN-NeerjaNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("output.mp3")
    os.system("start output.mp3")  # Windows

if __name__ == "__main__":
    text = input("Enter text to convert into speech: ")
    print("Select Voice:\n1. Neerja (Female)\n2. Prabhat (Male)")
    choice = input("Choose voice (1 or 2): ")

    if choice == '1':
        voice = "en-IN-NeerjaNeural"   # Female Indian English
    else:
        voice = "en-IN-PrabhatNeural"  # Male Indian English

    asyncio.run(text_to_speech(text, voice))
