import os

class Exfiltrator:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def send(self, bytes):
        with open(self.data_dict["file_name"], "ab") as f:
            f.write(bytes)

    def recv(self):
        result = None
        with open(self.data_dict["file_name"], "rb") as f:
            try:
                result = f.read()
            except:
                pass
        os.remove(self.data_dict["file_name"])
        return result
