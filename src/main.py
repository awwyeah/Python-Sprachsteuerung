import audiostream
import decoding_audio
import sys

# command line arguments
if sys.argv[1] == "record_raw":
    audiostream.record_raw(sys.argv[2])
elif sys.argv[1] == "record_wav":
    audiostream.record_wav(sys.argv[2])
elif sys.argv[1] == "play":
    audiostream.play(sys.argv[2])
elif sys.argv[1] == "decoding":
    decoding_audio.decoding(sys.argv[2])
elif sys.argv[1] == "live_decoding":
    decoding_audio.live_decoding()
elif sys.argv[1] == "decoding_test":
    decoding_audio.decoding_test(sys.argv[2])

