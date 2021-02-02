"""
conda install pyaudio

> python test_sound.py
#### Start ####
(start sound lasting 1 second)
After 2.5 seconds ...
#### End ####
(end sound lasting 1 second)
After 2.5 seconds ...
#### Start lasting 2 seconds ####
(start sound lasting 2 seconds)
"""

from Sound.sound_utilis import startRing, endRing
import time

print("#### Start ####")
startRing()

print("After 2.5 seconds ...")
time.sleep(2.5)

print("#### End ####")
endRing()

print("After 2.5 seconds ...")
time.sleep(2.5)

print("#### Start lasting 2 seconds ####")
startRing(duration = 2)