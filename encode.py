import sounddevice as sd
from scipy.io.wavfile import write


def record_audio():
    print(f'iniciando a gravação...')
    fs = 44100  # Sample rate
    seconds = 4  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('audio/example1.wav', fs, myrecording)  # Save as WAV file
    print(f'gravação finalizada')
