def girod_listen():
    # your code
    user_input = girod_listen()
def girod_listen():
    print("Inside girod_listen function")
    # ... rest of the code

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def respond(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
while True:
    user_input = listen()
    if user_input.lower() == 'exit':
        break
    response_text = respond(user_input)
    print("Girod:", response_text)
    speak(response_text)
    
    def respond(text, language='en'):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=150
    )
    response_text = response.choices[0].text.strip()

    if language == 'ar':
        # Translate the response to Arabic
        # Implement your translation logic here
        response_text = translate_to_arabic(response_text)

    return response_text

def speak(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("response.mp3")
    playsound.playsound("response.mp3")

# Example usage for bilingual support
user_input = listen(language='ar')  # Listen for Arabic input
response_text = respond(user_input, language='ar')  # Respond in Arabic
speak(response_text, language='ar')  # Speak the response in Arabic