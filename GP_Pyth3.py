import speech_recognition as sr
import google.generativeai as genai

# Constants for the AI Assistant API
HEADERS = {'Content-Type': 'application/json'}

genai.configure(api_key="Gemini Key here")
model = genai.GenerativeModel("gemini-1.5-flash")




def capture_audio():
    """
    Captures audio from the microphone and converts it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please ask your question.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected within the time limit.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None




def main():
    """
    Main function to run the program.
    """
    print("Welcome to meBot AI Assistant!")
    while True:
        # Capture user's audio input
        question = capture_audio()
        if not question:
            print("Unable to process your question. Try again.")
            continue

        # Send question to Ai
        response = model.generate_content(question)
        if question is not None:
            print(f"meBot says: {response.text}")
        else:
            print("Failed to get a response from meBot.")

        # Ask if the user wants to continue



if __name__ == "__main__":
    main()