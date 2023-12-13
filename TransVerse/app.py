import streamlit as st
from googletrans import Translator, LANGUAGES

def main():
    st.title("Transverse")
    
    # Tagline
    st.write("*Translate seamlessly across languages with Transverse.*")
    
    # User instructions
    st.sidebar.markdown("### Instructions:")
    st.sidebar.markdown("1. Enter the text you want to translate.")
    st.sidebar.markdown("2. Select the source language.")
    st.sidebar.markdown("3. Select the target language.")
    st.sidebar.markdown("4. Click the 'Translate' button.")
    
    # User input
    text_to_translate = st.text_area("Enter text to translate:")

    # Select source language
    source_language = st.selectbox("Select source language:", ["Auto Detect"] + list(LANGUAGES.values()))

    # Select target language
    target_language = st.selectbox("Select target language:", list(LANGUAGES.values()))

    # Translate button
    if st.button("Translate"):
        if text_to_translate:
            if source_language == "Auto Detect":
                source_language_code = "auto"
            else:
                source_language_code = [code for code, name in LANGUAGES.items() if name == source_language][0]
            
            target_language_code = [code for code, name in LANGUAGES.items() if name == target_language][0]
            
            translation_result = translate_text(text_to_translate, source_language_code, target_language_code)
            
            if translation_result:
                st.success(f"**Translated Text ({target_language}):**\n{translation_result}")
        else:
            st.warning("Please enter text to translate.")

def translate_text(text, source_language, target_language):
    try:
        translator = Translator()
        translation = translator.translate(text, src=source_language, dest=target_language)
        return translation.text
    except Exception as e:
        st.error(f"Translation error: {e}")
        return None

if __name__ == "__main__":
    main()
