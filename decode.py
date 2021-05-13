from utils import save_audio, filtro
from utils import normalize_wav, play_sound, low_pass_filter, calcFFT
import os
import scipy.io
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift

time = None
FS = 44100


def main():
    global time
    audio_path = 'audio/modulated2.wav'
    audioBuffer, time = read_wav(audio_path)
    sinal_desmodulado = desmodulando_wav(audioBuffer)
    filtrado = filtrando(sinal_desmodulado)
    play_sound(sinal_desmodulado, FS)


def read_wav(audio_path):
    # read wav
    wavedata = audio_path  # plot this wav file     ~/audio/aaa.wav
    sampleRate, audioBuffer = scipy.io.wavfile.read(wavedata)
    #audioBuffer = audioBuffer[:, 1]

    duration = len(audioBuffer)/sampleRate
    time = np.arange(0, duration, 1/sampleRate)  # time vector

    X, Y = calcFFT(audioBuffer, FS)
    fig = plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time, audioBuffer)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Wav Recebido')
    # fourier
    plt.subplot(2, 1, 2)
    limite_x = 24000
    plt.xlim(-limite_x, limite_x)
    plt.title("Fourier Do Sinal Original")
    plt.plot(X, np.abs(Y), 'red')
    fig.tight_layout(pad=2.0)

    plt.show()

    return audioBuffer, time


def filtrando(sinal_desmodulado):
    cuttoff = 4000  #
    filtered_wav = filtro(sinal_desmodulado, FS, cuttoff)

    return filtered_wav


def desmodulando_wav(sinal_modulado):
    # modulando
    # sinal_modulado = sinal_modulado[:, 0]
    portadora_freq = 14000  # hz
    portadora = np.cos(2*np.pi*portadora_freq*time)
    sinal_desmodulado = sinal_modulado * portadora

    X, Y = calcFFT(sinal_desmodulado, FS)
    fig = plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time, sinal_desmodulado)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Wav Modulado')
    # fourier
    plt.subplot(2, 1, 2)
    limite_x = 24000
    plt.xlim(-limite_x, limite_x)
    plt.title("Fourier Do Sinal Modulado")
    plt.plot(X, np.abs(Y), 'red')
    fig.tight_layout(pad=2.0)

    plt.show()

    return sinal_desmodulado


main()
