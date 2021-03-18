from base64 import b64encode
def base64_encode_str(s: str) -> str:
    s_byte = s.encode("utf-8")
    by = b64encode(s_byte)
    return by.decode("utf-8")
