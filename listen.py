# import speech_recognition as sr
# from googletrans import Translator
# import eel
# from speak import *

# def is_nepali(text):
#     nepali_characters = set("अ आ इ ई उ ऊ ए ऐ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह ा ि ी ु ू े ै ो ौ ्".split())
#     return any(char in nepali_characters for char in text)

# def listen_for_speech(recognizer):
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         eel.DisplayMessage("Listening.......🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤")
#         print("Listening........🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤")
#         audio = recognizer.listen(source)
#     return audio

# def recognize_text_from_audio(audio, recognizer):
#     try:
#         recognized_text = recognizer.recognize_google(audio, language="ne-NP")  # Set your language here en-in
#         return recognized_text
#     except sr.UnknownValueError:
#         return None
#     except sr.RequestError as e:
#         print(f"Request error: {e}")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# def translate_text(text):
#     translator = Translator()
#     translation = translator.translate(text, src="ne", dest="en")
#     return translation.text


# def recognize_speech():
#     recognizer = sr.Recognizer()
#     recognizer.dynamic_energy_threshold = False
#     recognizer.energy_threshold = 300  # Lower threshold to detect quieter sounds
#     recognizer.pause_threshold = 0.6  # Adjust pause threshold for your speaking style
#     recognizer.non_speaking_duration = 0.3


#     audio = listen_for_speech(recognizer)
#     recognized_text = recognize_text_from_audio(audio, recognizer)
    
#     if recognized_text:
#         eel.DisplayMessage("Recognizing text...")
#         print("Recognizing text:", end='', flush=True)
#         print(recognized_text)
#         eel.DisplayMessage(recognized_text)

#         if is_nepali(recognized_text):
#             translated_text = translate_text(recognized_text)
#             eel.DisplayMessage(translated_text)
#             print("Translated text:", end='', flush=True)
#             print(translated_text)
#             return translated_text
#         else:
#             eel.DisplayMessage(recognized_text)
#             print("You said: ", end='', flush=True)
#             print(recognized_text)
#             return recognized_text
#     else:
#         print("Sorry, I couldn't recognize any speech.")
#         eel.DisplayMessage("Sorry, I couldn't recognize any speech.")
        
#         return ""

import speech_recognition as sr
import eel
from speak import *


def listen_for_speech(recognizer):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        eel.DisplayMessage("Listening.......🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤")
        print("Listening........🎤🎤🎤🎤🎤🎤🎤🎤🎤🎤")
        audio = recognizer.listen(source)
    return audio


def recognize_text_from_audio(audio, recognizer):
    try:
        recognized_text = recognizer.recognize_google(audio, language="en-IN")
        return recognized_text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 300  # Lower threshold to detect quieter sounds
    recognizer.pause_threshold = 0.6  # Adjust pause threshold for your speaking style
    recognizer.non_speaking_duration = 0.3

    audio = listen_for_speech(recognizer)
    recognized_text = recognize_text_from_audio(audio, recognizer)

    if recognized_text:
        eel.DisplayMessage("Recognizing text...")
        print("Recognizing text:", end='', flush=True)
        print(recognized_text)
        eel.DisplayMessage(recognized_text)

        return recognized_text
    else:
        print("Sorry, I couldn't recognize any speech.")
        eel.DisplayMessage("Sorry, I couldn't recognize any speech.")

        return ""

