import importlib

class Combleaf:
    def __init__(self, module):
        config = importlib.import_module(module)
        self.send = config.send
        self.recv = config.recv

if __name__ == "__main__":
    localfile = Combleaf("modules.local_filewrite")
    localfile.send(b"hello")
    print(localfile.recv().decode())