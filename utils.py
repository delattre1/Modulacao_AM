from scipy.io.wavfile import write
from scipy import signal as sg
from scipy.fftpack import fft, fftshift
import numpy as np
import sounddevice as sd


def calcFFT(signal, fs):
    N = len(signal)
    T = 1/fs
    xf = np.linspace(-1.0/(2.0*T), 1.0/(2.0*T), N)
    yf = fft(signal)

    return(xf, fftshift(yf))


def normalize_wav(data):
    max = abs(data.max())
    min = abs(data.min())

    if max > min:
        max_abs = max
    else:
        max_abs = min
    # to be in range [-1,1]

    constant = 1/max_abs

    return data*constant


def play_sound(wav_array, fs):
    print('começando reproducao do audio')
    sd.play(wav_array, fs)
    sd.wait()
    print(f'finalizado!')


def filtro(y, samplerate, cutoff_hz):
  # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
    nyq_rate = samplerate/2
    width = 5.0/nyq_rate
    ripple_db = 60.0  # dB
    N, beta = sg.kaiserord(ripple_db, width)
    taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
    yFiltrado = sg.lfilter(taps, 1.0, y)

    return yFiltrado


def low_pass_filter(wav_array, cutoff_hz, fs):
    nyq_rate = fs/2
    width = 5.0/nyq_rate
    ripple_db = 60.0  # dB
    N, beta = sg.kaiserord(ripple_db, width)
    taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

    return(sg.lfilter(taps, 1.0, wav_array))


def save_audio(path, sinal):
    print(f'Salvando...')
    fs = 44100  # Sample rate
    write(path, fs, sinal)  # Save as WAV file
    print('Salvo!')


def record_audio(path):
    print(f'iniciando a gravação...')
    fs = 44100  # Sample rate
    seconds = 4  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(path, fs, myrecording)  # Save as WAV file
    print(f'gravação finalizada')
