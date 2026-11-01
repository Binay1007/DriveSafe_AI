import wave
import math
import struct

sample_rate = 44100
duration = 2  # seconds
frequency = 1000  # Hz
volume = 32767

wav = wave.open("alarm.wav", "w")
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(sample_rate)

for i in range(sample_rate * duration):
    value = int(volume * math.sin(2 * math.pi * frequency * i / sample_rate))
    wav.writeframes(struct.pack("<h", value))

wav.close()

print("alarm.wav created successfully!")