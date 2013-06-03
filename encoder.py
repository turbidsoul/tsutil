# -*- coding: utf8 -*-

__enc64__ = [
    'A', 'B', 'C', 'D', "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', "W", 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', "w", 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '='
]


__enc32__ = [
    'A', 'B', 'C', 'D', "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', "W", 'X', 'Y', 'Z',
    '2', '3', '4', '5', '6', '7', '='
]


__enc16__ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def base64_encode(data):
    """
    Base 64 encoder
    """
    total = len(data)
    result = []
    mod = 0
    for i in range(total):
        cur = ord(data[i])
        mod = i % 3
        if mod == 0:
            result.append(__enc64__[cur >> 2])
        elif mod == 1:
            prev = ord(data[i - 1])
            result.append(__enc64__[((prev & 3) << 4) | (cur >> 4)])
        elif mod == 2:
            prev = ord(data[i - 1])
            result.append(__enc64__[(prev & 0x0f) << 2 | cur >> 6])
            result.append(__enc64__[cur & 0x3f])
    if mod == 0:
        result.append(__enc64__[(cur & 3) << 4])
        result.append(__enc64__[64] * 2)
    elif mod == 1:
        result.append(__enc64__[(cur & 0x0f) << 2])
        result.append(__enc64__[64])
    return "".join(result)


def base64_decode(data):
    """
    Base 64 decoder
    """
    data = data.replace(__enc64__[64], '')
    total = len(data)
    result = []
    mod = 0
    for i in range(total):
        mod = i % 4
        cur = __enc64__.index(data[i])
        if mod == 0:
            continue
        elif mod == 1:
            prev = __enc64__.index(data[i-1])
            result.append(chr(prev << 2 | cur >> 4))
        elif mod == 2:
            prev = __enc64__.index(data[i-1])
            result.append(chr((prev & 0x0f) << 4 | cur >> 2))
        elif mod == 3:
            prev = __enc64__.index(data[i - 1])
            result.append(chr((prev & 3) << 6 | cur))

    return "".join(result)


def base16_encode(data):
    result = []
    for c in data:
        result.append(__enc16__[(ord(c) & 0xF0) >> 4])
        result.append(__enc16__[ord(c) & 0x0F])
    return "".join(result)


def base16_decode(data):
    result = []
    for i in range(0, len(data), 2):
        high = __enc16__.index(data[i])
        low = __enc16__.index(data[i + 1])
        result.append(chr(high << 4 | low))

    return "".join(result)