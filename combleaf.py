import importlib

class Combleaf:
    def __init__(self, module, data_dict=None):
        config = importlib.import_module(module)
        module_object = config.Exfiltrator(data_dict)
        self.send = module_object.send
        self.recv = module_object.recv
