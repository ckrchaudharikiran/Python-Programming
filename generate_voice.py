# pip install gtts
# pip install playsound==1.2.2
import gtts
import playsound
text = input("Enter something here: ")
sound = gtts.gTTS(text, lang = "en")
sound.save("Welcome.mp3")
playsound.playsound("Welcome.mp3")


# import gtts
# import playsound
# import time

# text = input("Enter something here: ")
# sound = gtts.gTTS(text, lang="en")

# filename = f"speech_{int(time.time())}.mp3"  # unique filename
# sound.save(filename)
# playsound.playsound(filename)


# import gtts
# import playsound

# try:
#     text = input("Enter something here: ")
#     sound = gtts.gTTS(text, lang="en")
#     sound.save("Welcome.mp3")
#     playsound.playsound("Welcome.mp3")
# except Exception as e:
#     print("Error:", e)
