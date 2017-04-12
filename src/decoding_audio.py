import pyaudio
import subprocess
from os import path, environ
import os

try:
    import sphinxbase
    import pocketsphinx as ps
except:
    print ("Pocket sphinx and sphixbase is not installed in your system. Please install it with package manager.")

MODELDIR = "/home/leon/Dokumente/Projekt/pocketsphinx/voxforge-de-r20140216/"
DATADIR = "/home/leon/Dokumente/Projekt/Sprachsteuerung/Python-Sprachsteuerung/src/"

# configure pocketsphinx
config = ps.Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'model_parameters/voxforge.cd_cont_4000'))
config.set_string('-lm', path.join(MODELDIR, 'cmusphinx-voxforge-de.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'etc/voxforge.dic'))

# creating decoding object
d = ps.Decoder(config)


def decoding_test(filename):
    d.start_utt()
    stream = open(filename, 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
            d.process_raw(buf, False, False)
        else:
            break
    d.end_utt()

    hypothesis = d.hyp()
    logmath = d.get_logmath()
    print ('Best hypothesis: ', hypothesis.hypstr, " model score: ", hypothesis.best_score, " confidence: ",
           logmath.exp(hypothesis.prob))
    output = []
    i = 0
    print ('Best hypothesis segments: ', [seg.word for seg in d.seg()])
    for seg in d.seg():
        output.append(seg.word)
    compare(output, filename)


# decoding audio file
def decoding(filename):

    # skip header of WAV-file
    wavFile = file(filename + '.wav', 'rb')
    wavFile.seek(44)

    # decoding audio file
    d.decode_raw(wavFile)
    results = d.hyp()

    # print decoded audiofile
    decode_speech = results[0]
    print decode_speech
    print results[1]


# live decoding
def live_decoding():

    # creating pyaudio object
    p = pyaudio.PyAudio()

    # input Stream
    in_stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    in_stream.start_stream()

    # start live decoding
    d.start_utt()
    while True:
        buf = in_stream.read(1024)
        d.process_raw(buf, False, False)
        results = d.get_hyp()
        #
        #
        break
    d.end_utt()


def compare(text, filename):
    #print text
    for x in text:
        if x == 'forward':
            if os.path.exists('hello_world.py'):
                full_path = os.path.abspath('hello_world.py')
                subprocess.call(['python', full_path])
        elif x == 'red':
            if os.path.exists('ledcolor.py'):
                full_path = os.path.abspath('ledcolor.py')
                subprocess.call(['python', full_path, '-c', 'red', '-d', '2'])
        elif x == 'blue':
            if os.path.exists('ledcolor.py'):
                full_path = os.path.abspath('ledcolor.py')
                subprocess.call(['python', full_path, '-c', 'blue', '-d', '2'])
        elif x == 'green':
            if os.path.exists('ledcolor.py'):
                full_path = os.path.abspath('ledcolor.py')
                subprocess.call(['python', full_path, '-c', 'green', '-d', '2'])
        elif x == 'play':
            if os.path.exists('audiostream.py'):
                full_path = os.path.abspath('audiostream.py')
                subprocess.call(['python', full_path, 'play', filename])