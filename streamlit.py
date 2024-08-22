import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

def qa(query_dict):
    # Placeholder function for the 'qa' function used in your code.
    # Replace this with your actual implementation.
    return {'result': f"Mock answer for query: {query_dict['query']}"}

def main():
    st.title("Speech/Text-based Query Answering App")

    st.write("Choose input method:")
    input_method = st.radio("Select method:", ("Text", "Audio"))

    if input_method == "Text":
        user_input = st.text_input("Input your query:")
    else:
        if st.button("Start Listening"):
            user_input = speech_to_text()
            st.write(f"You said: {user_input}")
        else:
            user_input = ""

    if user_input.lower() == "exit":
        st.write("Exiting...")
        text_to_speech("Exiting")
        st.stop()

    if user_input:
        result = qa({'query': user_input})
        st.write(f"Answer: {result['result']}")
        text_to_speech(result['result'])

if __name__ == "__main__":
    main()
