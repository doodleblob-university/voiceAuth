import argparse
from pathlib import Path

p = argparse.ArgumentParser(description="")
p.add_argument("-p", "--path", metavar="path", help="path to audio samples", default="./samples")


from VoiceAuth import VoiceAuth

def main(args):    
    VoiceAuth(Path(args.path))

if __name__ == "__main__":
    main( p.parse_args() )