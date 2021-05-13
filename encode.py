from utils import save_audio
from utils import normalize_wav, play_sound, low_pass_filter, calcFFT
import os
import scipy.io
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift

FS = 44100

time = None


def main():
    global time
    audioBuffer, time = read_wav()
    normalized_wav = norm_wav(audioBuffer)
    filtered_wav = filter_wav(normalized_wav)
    modulated_wav = modulate_wav(filtered_wav)
    save_audio('audio/modulated2.wav', modulated_wav)


def read_wav():
    # read wav
    wavedata = 'audio/example2.wav'  # plot this wav file     ~/audio/aaa.wav
    sampleRate, audioBuffer = scipy.io.wavfile.read(wavedata)
    audioBuffer = audioBuffer[:, 1]

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
    plt.xlim(-5000, 5000)
    plt.title("Fourier Do Sinal Original")
    plt.plot(X, np.abs(Y), 'red')
    fig.tight_layout(pad=2.0)

    plt.show()

    return audioBuffer, time


def norm_wav(audioBuffer):
    normalized_wav = normalize_wav(audioBuffer)
    X, Y = calcFFT(normalized_wav, FS)
    fig = plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time, normalized_wav)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Wav Normalizado')
    # fourier
    plt.subplot(2, 1, 2)
    plt.xlim(-5000, 5000)
    plt.title("Fourier Do Sinal Normalizado")
    plt.plot(X, np.abs(Y), 'red')
    fig.tight_layout(pad=2.0)

    plt.show()

    return normalized_wav


def filter_wav(normalized_wav):
    cuttoff = 4000  #
    filtered_wav = low_pass_filter(normalized_wav, cuttoff, FS)

    X, Y = calcFFT(filtered_wav, FS)
    fig = plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time, filtered_wav)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Wav Filtrado')
    # fourier
    plt.subplot(2, 1, 2)
    plt.xlim(-5000, 5000)
    plt.title("Fourier Do Sinal Filtrado")
    plt.plot(X, np.abs(Y), 'red')
    fig.tight_layout(pad=2.0)

    plt.show()

    return filtered_wav


def modulate_wav(filtered_wav):
    # modulando
    portadora_freq = 14000  # hz
    portadora = np.cos(2*np.pi*portadora_freq*time)
    sinal_modulado = filtered_wav * portadora

    X, Y = calcFFT(sinal_modulado, FS)
    fig = plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time, sinal_modulado)
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

    return sinal_modulado


main()
