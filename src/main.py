import audiostream
import decoding_audio
import sys

# command line arguments 
if sys.argv[1] == "record":
    audiostream.record(sys.argv[2])
elif sys.argv[1] == "output":
    audiostream.audio_output(sys.argv[2])
elif sys.argv[1] == "decoding":
    decoding_audio.decoding(sys.argv[2])
elif sys.argv[1] == "live_decoding":
    decoding_audio.live_decoding()

