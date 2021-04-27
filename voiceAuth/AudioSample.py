from pathlib import Path
import scipy.io.wavfile as wav

import numpy as np

from MFCCFeatures import MFCCFeatures as MFCC

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
        #TODO: VAD to isolate areas of voice activity
        #TODO: noise reduction

        self.features = np.hstack( (MFCC.getFeatures(self.rate, self.signal)) )

