import argparse
from pathlib import Path

p = argparse.ArgumentParser()
s = p.add_subparsers(help="Desired action to perform", dest="action")
pTrain = s.add_parser("train", help="train model")
pTrain.add_argument("-p", "--path", metavar="path", help="path to training samples", default=Path("./voiceAuth/samples"))
pTrain.add_argument("-g", "--gmmpath", metavar="model", help="path to gmm models", default=Path("./voiceAuth/models"))
pPredict = s.add_parser("predict", help="predict")
pPredict.add_argument("-i", "--input", metavar="voice", help="path to voice sample; if None, record voice", default=None)
pPredict.add_argument("-p", "--path", metavar="path", help="path to gmm models", default=Path("./voiceAuth/models"))

def main(args):    
    if( args.action == "train" ):
        from Train import Train
        Train( args.path, args.gmmpath )

    elif( args.action == "predict" ):
        from Predict import Predict
        Predict( args.input, args.path )

if __name__ == "__main__":
    args = p.parse_args()
    main( args )