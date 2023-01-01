import os


def send(bytes):
    with open("localfile.bytes", "ab") as f:
        f.write(bytes)

def recv():
    result = None
    with open("localfile.bytes", "rb") as f:
        try:
            result = f.read()
        except:
            pass
    os.remove("localfile.bytes")
    return result