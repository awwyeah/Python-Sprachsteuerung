import pocketsphinx as ps
#import sphinxbase
import pyaudio

# creating decoding object
hmmd = '/usr/share/pocketsphinx/model/hmm/wsj1'
lmd = '/usr/share/pocketsphinx/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP'
dictd = '/usr/share/pocketsphinx/lm/wsj/wlist5o.dic'
d = ps.Decoder(hmm=hmmd, lm=lmd, dict=dictd)


# decoding audio file
def decoding(filename):

    # skip header of WAV-file
    wavFile = file(filename + '.wav', 'rb')
    wavFile.seek(44)

    # decoding audio file
    d.decode_raw(wavFile)
    results = d.get_hyp()

    # takes first match
    decode_speech = results[0]
    print "I said ", decode_speech[0], " with a confidence of ", decode_speech[1]


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








