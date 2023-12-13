# Transverse - Language Translation Web App

**Transverse** is a simple web application built using Streamlit and the Google Translate API (`googletrans`). This application allows users to seamlessly translate text between different languages.
Visit Transverse: [https://transverse.onrender.com/](https://transverse.onrender.com/)
## Features

- **User-Friendly Interface:** The web app provides a clean and intuitive interface for users to interact with.
- **Auto Detection:** Users can choose to automatically detect the source language.
- **Language Selection:** Users can select both the source and target languages from a list of supported languages.
- **Translation Results:** The translated text is displayed, providing users with the translated content.

## How to Use

1. **Enter Text:**
   - Input the text you want to translate in the designated text area.

2. **Select Source Language:**
   - Choose the source language from the dropdown menu. You can also opt for automatic language detection.

3. **Select Target Language:**
   - Choose the target language from the dropdown menu.

4. **Translate:**
   - Click the "Translate" button to initiate the translation process.

5. **View Translation:**
   - The translated text will be displayed, indicating the target language.

## Instructions

1. **Installation:**
   - Ensure that you have Python installed.
   - Install the required packages using `pip install streamlit googletrans==4.0.0-rc1`.

2. **Run the Application:**
   - Execute the script using `streamlit run app.py` in the terminal.

3. **Use the Web App:**
   - Open the provided URL in your web browser to access the Transverse web application.
   - Follow the on-screen instructions to translate text.

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [googletrans](https://pypi.org/project/googletrans/)

## Notes

- This application relies on the Google Translate API, and it requires an internet connection to perform translations.
- In case of translation errors, an error message will be displayed on the screen.

Feel free to explore and enhance the Transverse web app to suit your translation needs!
