from pathlib import Path

from AudioSample import AudioSample
from ActivityDetection import ActivityDetection

class Train():

    def __init__(self, path):
        self.ad = ActivityDetection()
        audioSamples = self.loadSamples(path)

    def loadSamples(self, path):
        audioSamples = dict()
        for audiofile in [ x for x in self.samplePath.glob("*.wav") if x.is_file() ]:
            sample = AudioSample( audiofile, self.ad )
            try:
                audioSamples[ sample.name ].append( sample )
            except KeyError:
                audioSamples[ sample.name ] = [ sample ]
        return audioSamples

    def createModels(self, samples):
        


        pass