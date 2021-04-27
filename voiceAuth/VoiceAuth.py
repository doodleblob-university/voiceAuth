import scipy.io.wavfile as wave
from pathlib import Path

from AudioSample import AudioSample
from ActivityDetection import ActivityDetection

class VoiceAuth:
    def __init__(self, p=Path(".","samples")):
        self.ad = ActivityDetection()
        self.samplePath = p
        self.audioSamples = []
        self.loadSamples()

    def loadSamples(self):
        for audiofile in [ x for x in self.samplePath.glob("*.wav") if x.is_file() ]:
            self.audioSamples.append( AudioSample( audiofile, self.ad ) )

