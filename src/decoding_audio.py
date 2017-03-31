import pocketsphinx as ps
#import sphinxbase
import pyaudio

# pocketsphinx input parameter, you have to put you're own path
hmmd = '/home/leon/Dokumente/Projekt/pocketsphinx/cmusphinx-en-us-8khz-5.2'
lmd = '/home/leon/Dokumente/Projekt/pocketsphinx/en-us.lm.dmp'
dictd = '/usr/share/pocketsphinx/model/lm/en_US/cmu07a.dic'

# creating decoding object
d = ps.Decoder(hmm=hmmd, lm=lmd, dict=dictd)


# decoding audio file
def decoding(filename):

    # skip header of WAV-file
    wavFile = file(filename + '.wav', 'rb')
    wavFile.seek(44)

    # decoding audio file
    d.decode_raw(wavFile)
    results = d.get_hyp()

    # print decoded audiofile
    decode_speech = results[0]
    print decode_speech



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








