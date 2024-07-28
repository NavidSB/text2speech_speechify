import speech_recognition as sr
import vlc
import time
from selenium import webdriver
from g4f.client import Client
from g4f.Provider import RetryProvider, Liaobots, Blackbox
import g4f.debug
from text2speech_speechify import speechify

# Set up Chrome options to ignore certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Replace 'path/to/chromedriver' with the actual path to your ChromeDriver
driver = webdriver.Chrome(options=chrome_options)

def speech2text():
    r = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something!")

        # Play beep
        p = vlc.MediaPlayer("beep1.mp3")
        p.play()

        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        recognized_text = r.recognize_google(audio, language='fa-IR')
        print("Google Speech Recognition thinks you said: " + recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return speech2text()
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return speech2text()

def get_response_gpt(prompt): 
    g4f.debug.logging = True

    client = Client(
        provider=RetryProvider([Blackbox, Liaobots], shuffle=False)
    )
    chat_completion = client.chat.completions.create(
        model="GPT-4",
        messages=[{"role": "user", "content": prompt}],
    )
    response = chat_completion.choices[0].message.content
    print(f"CHAT GPT RESPONSE: {response}")
    return response

def main():
    # Create the SpeechHelper instance
    text2speech = speechify(driver, language="persian")
    
    while True:
        time.sleep(2)
        try:
            recognized_text = speech2text()
            time.sleep(1)
            prompt = "جواب سوال زیر را به زبان فارسی بگو: \n" + recognized_text
            new_description = get_response_gpt(prompt)
            time.sleep(1)
            text2speech.text2speech(new_description)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
