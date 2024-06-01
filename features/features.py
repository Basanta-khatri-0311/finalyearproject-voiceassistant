import os
from playsound import playsound
from speak import speak
import webbrowser
import requests
from selenium import webdriver
from googlesearch import search
import openai
from listen import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import pywhatkit as kit
from datetime import datetime, timedelta
from hugchat import hugchat
from facedetection import detected_face_name
import googletrans
from googletrans import Translator

# Initialize Chrome WebDriver (make sure to specify the path to your chromedriver)
# driver = webdriver.Chrome("/Users/basantkhatri/Downloads/chrome-mac-arm64")


def echostartsound():
    music_dir = "assets/sound/echostartvoice.mp3"
    speak("Loading system files")
    playsound(music_dir)
    print("Echo started........")



def open_website(text):
    # Split the recognized text based on the "open" keyword
    parts = text.split("open", 1)
    if len(parts) > 1:
        # Extract the text after "open" as the website name
        website_name = parts[1].strip().lower()
    
    if website_name:
        # Construct the URL based on the website name
        url = f"https://{website_name}.com"
        
        # Open the website in the default web browser
        speak(f"Opening {website_name}")
        webbrowser.open(url)
    else:
        speak("Please specify a website name")



def search_youtube(query):
    # Construct the YouTube search URL
    search_url = f"https://www.youtube.com/results?search_query={query}"

    # Speak only the search query
    speak(f"Searching in YouTube for {query}")
    webbrowser.open(search_url)


def play_video(text):
    # Extract the video query from the recognized text
    video_query = text.replace("play", "").replace("in youtube", "").strip()

    if video_query:
        # Use the YouTube API to search for videos
        api_url = "https://www.googleapis.com/youtube/v3/search"
        api_key = "AIzaSyBkZk8LpiTkZ0xLk3yBTd9p7eO0fnjRGEo"  # Replace with your own API key

        params = {
            "part": "snippet",
            "q": video_query,
            "type": "video",
            "key": api_key,
            "maxResults": 1
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        # Extract the video ID of the first result
        if "items" in data and data["items"]:
            video_id = data["items"][0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            # Open the YouTube video URL in the default web browser
            speak(f"Playing video: {video_query}")
            webbrowser.open(video_url)
        else:
            speak("No video found with the specified name")
    else:
        speak("Please specify a video to play")


def search_google(query):
    try:
        search_results = list(search(query, num_results=1))
        if search_results:
            webbrowser.open(search_results[0])
        else:
            speak("No search results found.")
    except Exception as e:
        speak("An error occurred while searching on Google.")
        print(f"Error: {e}")

def split_into_sentences(text):
    sentences = text.split('. ')
    sentences = [s + '.' for s in sentences if s]
    return sentences

def chatBot(query):
    user_input = query.lower()
    cookie_path = "features/cookies.JSON"
    try:
        chatbot = hugchat.ChatBot(cookie_path=cookie_path)
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        response = chatbot.chat(user_input)
        response = str(response)
        words = response.split()
        if len(words) > 30:
            sentences = split_into_sentences(response)
            truncated_response = ''
            word_count = 0
            for sentence in sentences:
                sentence_word_count = len(sentence.split())
                if word_count + sentence_word_count > 30:
                    break
                truncated_response += sentence + ' '
                word_count += sentence_word_count
            response = truncated_response.strip() + '...'
        else:
            response = response.strip()

        speak(response)
        eel.DisplayMessage(response)
        time.sleep(10)
        return response
    except Exception as e:
        speak("An error occurred while querying the chat bot.")
        print(f"Error: {e}")




def chatBotforProgram(query):
    user_input=query.lower()
    chatbot= hugchat.ChatBot(cookie_path="features/cookies.JSON")
    id=chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    response=str(response)
    speak("Sure sir here is what i found for your request")
    eel.DisplayMessage(response)
    time.sleep(10)
    return response




# Function to pause the video using Selenium
# def pause_video():
#     pause_button = driver.find_element_by_css_selector(".ytp-play-button")
#     pause_button.click()

# # Function to skip the video using Selenium
# def skip_video():
#     skip_button = driver.find_element_by_css_selector(".ytp-next-button")
#     skip_button.click()


def send_email(subject, message, to_email):
    # Email configuration
    email_sender = "basantkhatri107@gmail.com"  # Your email address
    email_password = "orwx zomv bbsd wfnl"  # Your email password

    # Create a MIMEText object to represent the email content
    email_body = MIMEText(message, "plain")

    # Create a MIMEMultipart object to represent the email
    email = MIMEMultipart()
    email["From"] = email_sender
    email["To"] = to_email
    email["Subject"] = subject

    # Attach the email content to the MIMEMultipart object
    email.attach(email_body)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, to_email, email.as_string())


def process_send_email_voice():
    while True:
        speak("Sure, Sir. Opening email. What is the subject of the email?")
        time.sleep(5)
        subject = recognize_speech().strip()
        if subject:
            break
        else:
            speak("I didn't catch that. Please tell me the subject of the email.")

    while True:
        speak("Please specify the message.")
        time.sleep(5)
        message = recognize_speech().strip()
        if message:
            break
        else:
            speak("I didn't catch that. Please tell me the message of the email.")

    while True:
        speak("Ok got it. To whom should I send this email?")
        time.sleep(5)
        to_email = recognize_speech().strip()
        to_email = format_email_address(to_email)
        if to_email:
            eel.DisplayMessage(f"Sending email to: {to_email}")
            break
        else:
            speak("I didn't catch that. Please tell me the email address of the recipient.")

    send_email(subject, message, to_email)
    time.sleep(2)
    speak("Email sent successfully!")
    eel.DisplayMessage("Email sent successfully!")

def format_email_address(raw_email):
    """Convert spoken email address to proper format"""
    raw_email = raw_email.lower()
    raw_email = re.sub(r"\s+at the rate\s+", "@", raw_email)
    raw_email = re.sub(r"\s+", "", raw_email)  # Remove any remaining spaces
    return raw_email

# Dictionary to map contact names to phone numbers
contacts = {
    "barsa": "+9779823371782",
    "ayush": "+9779845998964"
}

DEFAULT_COUNTRY_CODE = "+977"  # Change this to your default country code

def format_phone_number(raw_input):
    """Convert spoken phone number or contact name to proper format for WhatsApp"""
    print(f"Raw input received: {raw_input}")  # Debug statement
    raw_input = raw_input.lower().strip()
    
    # Check if the input is a name in the contacts dictionary
    if raw_input in contacts:
        number = contacts[raw_input]
        print(f"Contact name found: {raw_input} -> {number}")  # Debug statement
        return number
    
    # Otherwise, assume it's a phone number
    raw_input = re.sub(r"\s+", "", raw_input)  # Remove any remaining spaces
    print(f"Processed input: {raw_input}")  # Debug statement
    
    # Add country code if not present
    if not raw_input.startswith("+"):
        raw_input = DEFAULT_COUNTRY_CODE + raw_input
        print(f"Added country code: {raw_input}")  # Debug statement

    return raw_input

def send_whatsapp_message(contact, message):
    try:
        # Extract the current time
        now = datetime.now()
        # Schedule the message to be sent 1 minute from now to give enough time for the WhatsApp web to open
        send_time = now + timedelta(minutes=1)
        
        # Format the contact number
        contact = format_phone_number(contact)
        print(f"Formatted contact: {contact}")  # Debug statement

        # Use pywhatkit to send the WhatsApp message
        kit.sendwhatmsg(contact, message, send_time.hour, send_time.minute)
        speak(f"WhatsApp message scheduled to be sent to {contact} at {send_time.strftime('%H:%M')}")
        return True  # Indicate success
    except Exception as e:
        speak("An error occurred while sending the WhatsApp message.")
        print(f"Error: {e}")
        return False  # Indicate failure

def make_whatsapp_call(contact):
    try:
        # Format the contact number
        contact = format_phone_number(contact)
        print(f"Formatted contact: {contact}")  # Debug statement
        
        # Use pywhatkit to make the WhatsApp call
        kit.sendwhatmsg_instantly(contact, "This is a test call message.")
        speak(f"Making a WhatsApp call to {contact}")
        return True  # Indicate success
    except Exception as e:
        speak("An error occurred while making the WhatsApp call.")
        print(f"Error: {e}")
        return False  # Indicate failure

def process_send_whatsapp_message_voice():
    global detected_face_name

    if detected_face_name != "Basanta":
        speak("Sorry, but You are not authorized to use this feature.")
        return

    while True:
        speak("Sure, Sir. To whom should I send this WhatsApp message?")
        time.sleep(5)
        contact = recognize_speech().strip()
        formatted_contact = format_phone_number(contact)
        if formatted_contact:
            break
        else:
            speak("I didn't catch that. Please tell me the contact number of the recipient.")
    
    while True:
        speak("Please specify the message.")
        time.sleep(5)
        message = recognize_speech().strip()
        if message:
            break
        else:
            speak("I didn't catch that. Please tell me the message.")

    if send_whatsapp_message(formatted_contact, message):
        speak("WhatsApp message sent successfully!")

def process_make_whatsapp_call_voice():
    while True:
        speak("Sure, Sir. To whom should I make this WhatsApp call?")
        time.sleep(5)
        contact = recognize_speech().strip()
        formatted_contact = format_phone_number(contact)
        if formatted_contact:
            break
        else:
            speak("I didn't catch that. Please tell me the contact number of the recipient.")

    # Make the WhatsApp call and check for success
    if make_whatsapp_call(formatted_contact):
        speak("WhatsApp call initiated successfully!")


    


def get_weather(city_name):
    api_key = "ed6b0a470f6bf404311f3eaeb21f1d63"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete API URL
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Get the response from the API
    response = requests.get(complete_url)
    data = response.json()
    
    # Check if the city was found
    if data["cod"] != "404":
        # Extracting data from the JSON response
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # Formulate the weather report
        weather_report = (f"Current temperature in {city_name} is {temperature}°C with "
                          f"{weather_description}. The humidity is {humidity}% and "
                          f"the atmospheric pressure is {pressure} hPa.")
        
        # Speak the weather report
        speak(weather_report)
        print(weather_report)
        return weather_report
    else:
        error_message = f"City {city_name} not found."
        speak(error_message)
        print(error_message)
        return error_message

def extract_city_name(text):
    words = text.split("of", 1)
    if len(words) > 1:
        city_name = words[1].strip()
        return city_name
    return None

def process_get_weather_voice():
    city_name = None
    
    while not city_name:
        speak("Please tell me the city name.")
        city_name = recognize_speech().strip()
        if not city_name:
            speak("I didn't catch that. Please tell me the city name again.")
    
    # Get the weather information
    get_weather(city_name)

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        speak("An error occurred while translating the text.")
        print(f"Error: {e}")
        return None

def get_language_code(language_name):
    languages = googletrans.LANGUAGES
    for code, name in languages.items():
        if name.lower() == language_name.lower():
            return code
    return None

def process_translation_request(text):
    if "to" in text:
        parts = text.split("to")
        text_to_translate = parts[0].replace("translate", "").strip()
        target_language = parts[1].strip()
        language_code = get_language_code(target_language)
        if language_code:
            translated_text = translate_text(text_to_translate, language_code)
            if translated_text:
                speak(f"The translated text is: {translated_text}")
                print(f"Translated text: {translated_text}")
            else:
                speak("Sorry, I couldn't translate the text.")
        else:
            speak("I didn't recognize the language. Please specify the language again.")
    else:
        speak("Please specify the text to translate.")
        text_to_translate = recognize_speech().strip()
        if text_to_translate:
            speak("Which language do you want to translate to?")
            target_language = recognize_speech().strip()
            language_code = get_language_code(target_language)
            if language_code:
                translated_text = translate_text(text_to_translate, language_code)
                if translated_text:
                    speak(f"The translated text is: {translated_text}")
                    print(f"Translated text: {translated_text}")
                else:
                    speak("Sorry, I couldn't translate the text.")
            else:
                speak("I didn't recognize the language. Please specify the language again.")
        else:
            speak("I didn't catch that. Please specify the text to translate.")

def process_translation_voice():
    speak("Please specify the text you want to translate.")
    time.sleep(1)
    text_to_translate = recognize_speech().strip()
    if not text_to_translate:
        speak("I didn't catch that. Please tell me the text to translate.")
        return

    speak("Which language do you want to translate to?")
    time.sleep(1)
    target_language = recognize_speech().strip()
    language_code = get_language_code(target_language)
    if not language_code:
        speak("I didn't catch that or the language is not supported. Please tell me the language again.")
        return

    translated_text = translate_text(text_to_translate, language_code)
    if translated_text:
        speak(f"The translated text is: {translated_text}")
        DisplayMessage(f"The translated text is: {translated_text}")
        print(f"Translated text: {translated_text}")
        DisplayMessage(f"Translated text: {translated_text}")
    else:
        speak("Sorry, I couldn't translate the text.")