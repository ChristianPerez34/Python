# create an applition that produces Do Re Mi Fa Sol La Si of the Solfege.
import winsound
frequencies = [261, 293, 329, 349, 392, 440, 493, 587]
duration = 500
for i in frequencies:
    winsound.Beep(i, duration)
