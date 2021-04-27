import numpy as np
from pathlib import Path

import pickle
from sklearn.mixture import GaussianMixture as GMM

from AudioSample import AudioSample
from ActivityDetection import ActivityDetection

class Train():

    def __init__(self, path, models):
        self._models = models
        self.ad = ActivityDetection()
        audioSamples = self.loadSamples(path)
        self.createModels(audioSamples)

    def loadSamples(self, path):
        audioSamples = dict()
        for audiofile in [ x for x in path.glob("*.wav") if x.is_file() ]:
            sample = AudioSample( audiofile, self.ad )
            try:
                audioSamples[ sample.name ].append( sample )
            except KeyError:
                audioSamples[ sample.name ] = [ sample ]
        return audioSamples

    def createModels(self, samples):
        for user in samples:
            features = np.asarray(())
            for sample in samples[user]:

                sampleFeatures = sample.features
                
                if( features.size == 0 ):
                    features = sampleFeatures
                else:
                    try:
                        features = np.vstack((features, sampleFeatures))
                    except ValueError:
                        pass #print("MISMATCH")
            
            #TODO: optimise gmm parameters
            # tied seems to work better but takes longer
            gmm = GMM(n_components=200, covariance_type="tied", max_iter = 2048, n_init=3)
            gmm.fit(features)
            #self._dumpModel(gmm, user)

            """ TESTING
            predict = AudioSample( "./voiceAuth/testing/cbwake0.wav", self.ad )
            pfeatures = predict.features
            
            scores = np.array(gmm.score(pfeatures))
            loglike = round(scores.sum(), 3)

            print(user, loglike)
            """


    def _dumpModel(self, model, user):
        modelpath = Path( self._models, user + ".gmm")
        pickle.dump(model, open( modelpath, "wb+" ))
