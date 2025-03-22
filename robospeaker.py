import pyttsx3
#engine is name of variable which store the output of pyttsx3
engine = pyttsx3.init()
#pyttsx3 is a library which starts\initialize the engine variable
text = input("Enter what you want to say: ")
engine.say(text)
#with the help of runandwait we tells the computer stop when you complete the speech
engine.runAndWait()



s