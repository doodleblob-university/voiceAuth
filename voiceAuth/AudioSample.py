from pathlib import Path
import scipy.io.wavfile as wav

import numpy as np

class AudioSample:
    def __init__(self, path, ad):
        self.ad = ad
        self.name, self.rate, self.signal = self.loadFile(path)
        self.__processSignal()

    def loadFile(self, path):
        name = Path(Path(path).stem).stem
        rate, data = wav.read(path)
        # get mono audio if not already
        if data.ndim > 1:
            data = data[:,0]
        return name, rate, data

        
    def __processSignal(self):
        # https://www.kaggle.com/ilyamich/mfcc-implementation-and-tutorial
        #TODO: VAD to isolate areas of voice activity

        #TODO: Apply MFCC (and LPC?)
        #fextractor = FeaturesExtractor()
        #features = fextractor.extract_features(self.signal, self.rate)

        pass
        
        
