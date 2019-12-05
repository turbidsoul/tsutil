import time
import hashlib
import base64
import struct
import hmac

def get_google_code(secret: str) -> str:
  time_idx = int(time.time()) // 30
  mac_hash = hmac.new(base64.b32decode(secret, True), struct.pack('>Q', time_idx), hashlib.sha1).digest()
  offset = mac_hash[19] & 0xF
  t = (struct.unpack('>I', mac_hash[offset: offset + 4])[0] & 0x7FFFFFFF) % 1000000
  return '{:0>6}'.format(t)
