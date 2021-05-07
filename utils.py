

import sounddevice as sd


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


def low_pass_filter(wav_array, cutoff_hz, fs):
    from scipy import signal as sg
    nyq_rate = fs/2
    width = 5.0/nyq_rate
    ripple_db = 120.0  # dB
    N, beta = sg.kaiserord(ripple_db, width)
    taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

    return(sg.lfilter(taps, 1.0, wav_array))
