# README.md # Speechify text to speech

This repository contains a Python script for converting text to speech using the Speechify web service. The script leverages Selenium to interact with the Speechify website and supports multiple languages, including Persian, Spanish, French, German, Afrikaans, and Arabic.

## Features

- Convert text to speech in various languages.
- Automatically handle pop-up windows.
- Ensure the text is pasted correctly before converting.
- Monitor the progress of the speech conversion.

## Installation

1. Download library and save to path file:
2. Install the required Python packages:
   ```sh
   pip install selenium
   ```

3. Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it's in your system PATH.

## Usage

To use the script, create an instance of the `speechify` class, specifying the desired language (default is Persian). Then, call the `text2speech` method with the text you want to convert to speech.

```python
from speechify import speechify

# Initialize the speechify class with the desired language
sp = speechify(language='english')

# Convert text to speech
sp.text2speech("Hello, this is a test of the text-to-speech functionality.")

