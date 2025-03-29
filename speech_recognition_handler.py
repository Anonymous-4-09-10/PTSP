import speech_recognition as sr
from fuzzywuzzy import process

class SpeechRecognition:
    def __init__(self):
        self.valid_distributions = ["gaussian", "laplacian", "uniform", "normal", "binomial", "rayleigh", "raili", "exponential", "poisson"]

    def get_distribution_from_voice(self):
        recognizer = sr.Recognizer()

        # Provide feedback for the user to speak
        print("Listening... Please say a distribution (e.g., Gaussian, Laplacian, etc.)")

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google Web Speech API
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")

            # Use fuzzy matching to find the closest match from the valid distributions
            best_match = process.extractOne(command, self.valid_distributions)

            if best_match[1] > 70:  # If match score is greater than 70, we accept it
                print(f"Best match: {best_match[0]}")
                return best_match[0]
            else:
                print("No close match found.")
                return None

        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return None

