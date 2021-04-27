from sklearn import preprocessing
from python_speech_features import mfcc
from python_speech_features import delta

class MFCCFeatures():
    FFTsize = 2048

    @staticmethod
    def getFeatures(rate, signal):
        
        mfccf = mfcc(signal, rate, nfft=MFCCFeatures.FFTsize)

        mfccFeature = preprocessing.scale(mfccf)
        deltas = delta(mfccf, 2)
        #ddeltas = delta(deltas, 2)

        return mfccFeature, deltas