from pathlib import Path
import scipy.io.wavfile as wav

class AudioSample:
    def __init__(self, path):
        self.path = path
        self.__loadFile()

    def __loadFile(self):
        self.name = Path(self.path.stem).stem
        self.rate, self._data = wav.read(self.path)
        print(self.name)

        