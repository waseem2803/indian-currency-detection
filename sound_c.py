import playsound
from pathlib import Path
import os

class Sound:
    def soundplay(currency):
        SCRIPT_DIR = Path(__file__).parent
        if currency == "10":
            t1 = SCRIPT_DIR / 'audio/01.mp3'
            playsound.playsound(t1)
        elif currency == "20":
            t2 = SCRIPT_DIR / 'audio/02.mp3'
            playsound.playsound(t2)
        elif currency == "50":
            t3 = SCRIPT_DIR / 'audio/03.mp3'
            playsound.playsound(t3)
        elif currency == "100":
            t4 = SCRIPT_DIR / 'audio/04.mp3'
            playsound.playsound(t4)
        elif currency == "200":
            t5 = SCRIPT_DIR / 'audio/05.mp3'
            playsound.playsound(t5)
        elif currency == "500":
            t6 = SCRIPT_DIR / 'audio/06.mp3'
            playsound.playsound(t6)
        elif currency == "2000":
            t7 = SCRIPT_DIR / 'audio/07.mp3'
            playsound.playsound(t7)
        else:
            t8 = SCRIPT_DIR / 'audio/in.mp3'
            playsound.playsound(t8)