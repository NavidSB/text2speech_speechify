# README.md

## Project Overview

This project integrates various tools and libraries to create an interactive voice-controlled system capable of recognizing speech in Persian, generating responses using the GPT-4 model, and converting text responses back into speech. The primary components include speech recognition, text-to-speech conversion, and interaction with an AI model for generating responses.

## Key Features

1. **Speech Recognition**:
   - Uses the `speech_recognition` library to capture audio input from a microphone and convert it to text using Google Speech Recognition.

2. **Text-to-Speech**:
   - Utilizes the `text2speech_speechify` module to convert text responses back into speech.

3. **AI Response Generation**:
   - Employs the GPT-4 model via the `g4f.client` library to generate AI-based responses to user queries.

4. **Browser Automation**:
   - Uses `selenium` to handle browser operations, configured to run in headless mode and ignore certificate errors.

## Requirements

- Python 3.x
- `speech_recognition`
- `vlc`
- `selenium`
- `g4f`
- `text2speech_speechify`
- ChromeDriver (configured path)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python packages:
   ```bash
   pip install speech_recognition python-vlc selenium g4f
   ```

3. Download and configure ChromeDriver:
   - Download from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Place it in a known directory and update the script with the correct path.

## Usage

1. **Run the Script**:
   - Ensure your microphone is connected and working.
   - Execute the script:
     ```bash
     python main.py
     ```

2. **Interaction**:
   - The system will prompt you to say something.
   - It will recognize your speech, generate a response using GPT-4, and then speak the response back to you in Persian.

## Code Structure

- **`main.py`**: Contains the main script with functions for speech recognition, AI response generation, and text-to-speech conversion.
  - `speech2text()`: Captures and recognizes speech.
  - `get_response_gpt(prompt)`: Generates a response using GPT-4.
  - `main()`: Main loop that orchestrates the interaction.

## Troubleshooting

- **Speech Recognition Errors**:
  - Ensure your microphone is properly configured.
  - Check your internet connection for Google Speech Recognition API requests.

- **ChromeDriver Issues**:
  - Ensure ChromeDriver is in the correct path and is compatible with your Chrome version.
  - Check ChromeDriver and browser compatibility.

- **General Errors**:
  - Review console output for specific error messages.
  - Ensure all required libraries are installed and up-to-date.

## License

This project is licensed under the MIT License.

---

Feel free to customize and extend this project to fit your specific needs. Contributions and feedback are welcome!
