import pyttsx3
process=pyttsx3.init()
text=input("Enter what you want to speak:")
process.say(text)
process.runAndWait()
