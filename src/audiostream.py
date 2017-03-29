import pyaudio
import wave

# buffer block size in byte
CHUNK = 1024

# audio format
FORMAT = pyaudio.paInt16

# channels
CHANNELS = 1

# sample rate
RATE = 16000

# recording seconds
RECORD_SECS = 5


# recording audio
def record(filename):

    # filename
    WAVE_OUTPUT_FILENAME = filename + ".wav"

    # initializing pyaudio object
    p = pyaudio.PyAudio()

    # input stream
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("recording..")

    # temporary buffer
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finish recording")

    # stop and close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # writing the recording in file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# play audio file
def audio_output(filename):

    # open file
    wf = wave.open((filename + ".wav"), "rb")

    # initializing pyaudio object
    p = pyaudio.PyAudio()

    # output stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    # read and play file
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop and close stream
    stream.stop_stream()
    stream.close()
    p.terminate()
