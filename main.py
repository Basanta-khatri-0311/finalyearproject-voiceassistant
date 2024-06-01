# import os
# import eel
# from features.features import *
# from speak import *
# from listen import *
# from qna import *
# import facedetection

# eel.init("gui")

# def start_recognition_loop():
#     # Add a delay to avoid potential race conditions during startup
#     time.sleep(3)
#     while True:
#         text = recognize_speech().lower()  # Capture speech input and convert to lowercase
#         if text:  # If text is recognized, process it
#             if "hello" in text or "hi" in text:
#                 speak("Hello there. How can i help you")
#                 # Check if the recognized text is in the dataset
#             elif "pause yourself" in text:
#                 pass  # Placeholder to skip processing
#             elif "stop yourself" in text:
#                 break  # Exit the loop when "stop yourself" is recognized
#             else:
#                 words = text.split()  # Split the text into words
#                 if "end" in words or "exit" in words :  # Check if "end" is one of the words
#                     speak("Sure sir. Feel free to call me again for any kind of help. See you soon")
#                     eel.DisplayMessage("Byeee see you soonn.....👋👋👋👋👋👋👋👋👋👋")
#                     time.sleep(6)
#                     eel.close_page()
#                     break
#                 elif "open" in text:
#                     open_website(text)
#                 elif "translate" in text:
#                     process_translation_voice(text)
#                 elif "google" in text:
#                     text = text.replace("what is", "").strip()
#                     search_google(text)
#                     speak("Here is what i found for you in google")
#                 elif "what is" in text or "tell me about" in text or "who is" in text or "i want to know" in text:
#                     chatBot(text)
#                 elif "program" in text:
#                     chatBotforProgram(text)
#                 elif "send mail" in text:
#                     process_send_email_voice()
#                 elif "about" in text:
#                     search_chatgpt(text)
#                 elif "search" in text and "in youtube" in text:
#                     search_query = text.replace("search", "").replace("in youtube", "").strip()
#                     search_youtube(search_query)
#                 elif "send whatsapp message" in text or "send a whatsapp message" in text:
#                     process_send_whatsapp_message_voice()
#                 elif "make whatsapp call" in text or "make a whatsapp call" in text:
#                     process_make_whatsapp_call_voice()
#                 elif "play" in text and "in youtube" in text:
#                     play_video(text)
#                 elif "weather" in text or "temperature" in text:
#                     city = extract_city_name(text)
#                     if not city:
#                         process_get_weather_voice()
#                     else:
#                         get_weather(city)
#                 else:
#                     best_answer = predict_answer(text, encoded_dataset, tokenizer, model)
#                     if best_answer:
#                         speak(best_answer)
#                     else:
#                         speak("Command not recognized")
                        
#         time.sleep(0.5)  # Small delay to avoid overwhelming the recognizer
        

# def start_eel():
#   eel.start('index.html',  size=(1920, 1080))


# def main():
#   if facedetection.performFaceDetection():
#     print('Application loading..........')
#     echostartsound()
#     time.sleep(1)
#     speak("Files loaded successfully")
#     time.sleep(1)
#     eel.DisplayMessage("Welcome to the virtual assistant. My name is ECHO. How can I help you sir...")
#     speak("Welcome to the virtual assistant. My name is ECHO. How can I help you sir...")
#     recognition_thread = threading.Thread(target=start_recognition_loop, daemon=True)
#     recognition_thread.start()
#     start_eel()

# if __name__ == "__main__":
#     main()


import os
import eel
from features.features import *
from speak import *
from listen import *
from qna import *
import facedetection
import threading
import time

eel.init("gui")

def start_recognition_loop():
    # Add a delay to avoid potential race conditions during startup
    time.sleep(3)
    while True:
        text = recognize_speech().lower()  # Capture speech input and convert to lowercase
        print(f"Recognized speech: {text}")  # Debug: Print recognized text
        if text:  # If text is recognized, process it
            words = text.split()  # Split the text into words
            if "end" in words or "exit" in words:  # Check if "end" or "exit" is one of the words
                print("Ending the session")  # Debug
                speak("Sure sir. Feel free to call me again for any kind of help. See you soon")
                eel.DisplayMessage("Byeee see you soonn.....👋👋👋👋👋👋👋👋👋👋")
                time.sleep(6)
                eel.close_page()
                break
            elif "open" in text:
                print("Opening website")  # Debug
                open_website(text)
            elif "translate" in text or "translator" in text:
                print("Translating text")  # Debug
                process_translation_voice()
            elif "google" in text:
                print("Performing Google search")  # Debug
                text = text.replace("what is", "").strip()
                search_google(text)
                speak("Here is what I found for you on Google")
            elif any(keyword in text for keyword in ["tell me about", "who is"]):
                print("Processing chatbot request")  # Debug
                chatBot(text)
            elif "program" in text:
                print("Processing program request")  # Debug
                chatBotforProgram(text)
            elif "send mail" in text:
                print("Sending email")  # Debug
                process_send_email_voice()
            elif "about" in text:
                print("Searching ChatGPT")  # Debug
                search_chatgpt(text)
            elif "search" in text and "in youtube" in text:
                print("Searching YouTube")  # Debug
                search_query = text.replace("search", "").replace("in youtube", "").strip()
                search_youtube(search_query)
            elif any(keyword in text for keyword in ["send whatsapp message", "send a whatsapp message"]):
                print("Sending WhatsApp message")  # Debug
                process_send_whatsapp_message_voice()
            elif any(keyword in text for keyword in ["make whatsapp call", "make a whatsapp call"]):
                print("Making WhatsApp call")  # Debug
                process_make_whatsapp_call_voice()
            elif "play" in text and "in youtube" in text:
                print("Playing YouTube video")  # Debug
                play_video(text)
            elif "weather" in text or "temperature" in text:
                print("Checking weather")  # Debug
                city = extract_city_name(text)
                if not city:
                    process_get_weather_voice()
                else:
                    get_weather(city)
            else:
                print("Finding best answer")  # Debug
                best_answer = predict_answer(text, encoded_dataset, tokenizer, model)
                if best_answer:
                    print(f"Best answer found: {best_answer}")  # Debug
                    speak(best_answer)
                else:
                    print("Command not recognized")  # Debug
                    speak("Command not recognized")
        time.sleep(0.5)  # Small delay to avoid overwhelming the recognizer

def start_eel():
    eel.start('index.html', size=(1920, 1080))

def main():
    if facedetection.performFaceDetection():
        print('Application loading..........')
        echostartsound()
        time.sleep(1)
        speak("Files loaded successfully")
        time.sleep(1)
        eel.DisplayMessage("Welcome to the virtual assistant. My name is ECHO. How can I help you sir...")
        speak("Welcome to the virtual assistant. My name is ECHO. How can I help you sir...")
        recognition_thread = threading.Thread(target=start_recognition_loop, daemon=True)
        recognition_thread.start()
        start_eel()

if __name__ == "__main__":
    main()
