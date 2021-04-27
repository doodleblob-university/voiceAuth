import scipy.io.wavfile as wave
from pathlib import Path

from AudioSample import AudioSample

class VoiceAuth:
    def __init__(self, p=Path(".","samples")):
        self.samplePath = p
        self.loadSamples()

    def loadSamples(self):
        for audiofile in [ x for x in self.samplePath.glob("*.wav") if x.is_file() ]:
            AudioSample(audiofile)

