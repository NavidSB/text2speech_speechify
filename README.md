# text2speech_speechify
convert texts to speech via speechify.com


# Speech Recognition and Text-to-Speech Integration

This project combines speech recognition, GPT-4 based language processing, and text-to-speech functionalities to create an interactive voice-driven application. The application captures audio input, processes it using Google Speech Recognition, generates a response using GPT-4, and then converts the response back to speech.

## Features

- **Speech Recognition**: Utilizes Google Speech Recognition to convert spoken Persian (fa-IR) into text.
- **GPT-4 Integration**: Sends the recognized text as a prompt to GPT-4, generating a natural language response in Persian.
- **Text-to-Speech**: Converts the GPT-4 response back into speech using the Speechify API.

## Requirements

- Python 3.x
- `speech_recognition` library
- `vlc` library
- `selenium` library
- `g4f` library
- `text2speech_speechify` library
- ChromeDriver (compatible with your version of Chrome)

## Installation

1. Install the required Python libraries:

    ```sh
    pip install speechrecognition python-vlc selenium g4f text2speech_speechify
    ```

2. Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it matches your version of Chrome. Update the script with the path to your ChromeDriver.

## Usage

1. Ensure you have a microphone connected to your system.
2. Run the script:

    ```sh
    python script_name.py
    ```

3. The application will prompt you to speak. After capturing your speech, it will process and respond using the integrated GPT-4 and text-to-speech functionalities.

## Code Overview

### Chrome Options Setup

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=chrome_options)
```

### Speech Recognition Function

```python
def speech2text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        p = vlc.MediaPlayer("beep1.mp3")
        p.play()
        audio = r.listen(source)

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
```

### GPT-4 Response Function

```python
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
```

### Main Function

```python
def main():
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
```

This script continuously listens for speech, processes it, and provides a spoken response, creating an interactive and user-friendly experience.
