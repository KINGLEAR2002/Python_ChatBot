import openai
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "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"

def chatbot_response(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input_text,
        max_tokens=1024,
        temperature=0.5,
        n=1  # Convert 'n' to integer
    )
    return response.choices[0].text

while True:
    user_choice = input("Choose mode: 1 (Speak) or 2 (Write): ")

    if user_choice == "1":
        with sr.Microphone() as source:
            print("Speak now ...")
            voice = listener.listen(source)
            data = listener.recognize_google(voice)
    elif user_choice == "2":
        data = input("Enter your message: ")
    else:
        print("Invalid choice. Please choose either 1 or 2.")
        continue

    if "exit" in data:
        break

    response_text = chatbot_response(data)

    choice = input("Press 1 to print the response or press 2 to print and hear it: ")
    if choice == "1":
        print(response_text)
    elif choice == "2":
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
    else:
        print("Invalid choice.")

    repeat = input("Do you want to continue again? (yes/no): ")
    if repeat.lower() in ["no", "n"]:
        break



