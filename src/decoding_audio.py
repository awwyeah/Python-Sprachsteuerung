import pocketsphinx as ps
#import sphinxbase
import pyaudio

# Decoding-Objekt erstellen
hmmd = '/usr/share/pocketsphinx/model/hmm/wsj1'
lmd = '/usr/share/pocketsphinx/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP'
dictd = '/usr/share/pocketsphinx/lm/wsj/wlist5o.dic'
d = ps.Decoder(hmm=hmmd, lm=lmd, dict=dictd)


# Audiodatei dekodieren
def decoding(filename):

    # Header der WAV-Datei ueberspringen
    wavFile = file(filename + '.wav', 'rb')
    wavFile.seek(44)

    # Audio Datei dekodieren
    d.decode_raw(wavFile)
    results = d.get_hyp()

    #
    decode_speech = results[0]
    print "I said ", decode_speech[0], " with a confidence of ", decode_speech[1]


# Live-Dekodierung
def live_decoding():

    # PyAudio-Objekt erzeugen
    p = pyaudio.PyAudio()

    # input Stream
    in_stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    in_stream.start_stream()

    # Dekodierung starten
    d.start_utt()
    while True:
        buf = in_stream.read(1024)
        d.process_raw(buf, False, False)
        results = d.get_hyp()
        #
        #
        break
    d.end_utt()








