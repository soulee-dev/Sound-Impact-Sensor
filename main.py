import sounddevice as sd
import numpy as np
from pynput.keyboard import Key, Controller

duration = 100000  # seconds
keyboard = Controller()

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) >= 250:
        print("함정카드 발동!!")
        keyboard.press('f')
        keyboard.release('f')

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
