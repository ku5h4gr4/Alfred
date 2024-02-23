import random
import webbrowser
from time import sleep
import pyautogui as pyg
def playlist():
    song_seq = (1, 2, 3, 4)
    suffle_song = random.choice(song_seq)
    if suffle_song == 1:
        webbrowser.open("https://www.youtube.com/watch?v=6QYcd7RggNU")
        sleep(1)
        pyg.press("k")

    elif suffle_song == 2:
        webbrowser.open("https://www.youtube.com/watch?v=mdb8L87DU58")
        sleep(1)
        pyg.press("k")
    elif suffle_song == 3:
        webbrowser.open("https://www.youtube.com/watch?v=_WW-TJL-TmI")
        sleep(1)
        pyg.press("k")
    else:
        webbrowser.open("https://www.youtube.com/watch?v=oyFobb9_dlg")
        sleep(1)
        pyg.press("k")