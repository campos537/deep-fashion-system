import base64

def get_result(result):
    stream = base64.decodebytes(result)
    return stream.decode()
    