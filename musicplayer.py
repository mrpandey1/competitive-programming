from pygame import mixer
mixer.init()
mixer.music.load("kalank.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
        print("press p to pause and r to resume")
        print("press e to exit")
        query=input(">>> ")
        if query == 'p':
                mixer.music.pause()
        elif query == 'r':
                mixer.music.unpause()
        elif query == 'e':
                mixer.music.stop()
                break
