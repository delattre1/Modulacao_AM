from utils import normalize_wav, play_sound, low_pass_filter
import os
import scipy.io
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

wavedata = 'audio/example1.wav'  # plot this wav file     ~/audio/aaa.wav


sampleRate, audioBuffer = scipy.io.wavfile.read(wavedata)
audioBuffer = audioBuffer[:, 1]

duration = len(audioBuffer)/sampleRate

time = np.arange(0, duration, 1/sampleRate)  # time vector

plt.figure(figsize=(8, 8))
plt.plot(time, audioBuffer)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('myAudioFilename')
plt.show()


normalized_wav = normalize_wav(audioBuffer)
fs = 44100
cuttoff = 4000  # hz
filtered_wav = low_pass_filter(normalized_wav, cuttoff, fs)

play_sound(audioBuffer, fs)
play_sound(normalized_wav, fs)
play_sound(filtered_wav, fs)
