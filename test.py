# -*- coding: utf8 -*-
from math2 import leibniz_pi, wallis_pi
from encoder import morse_encode, morse_decode


def test_math2():
    print(leibniz_pi(9999999))
    print(wallis_pi(9999999))


def test_encoder():
    result = morse_encode('4194418141634192622374')
    print(result)

    result = morse_decode(result)
    print(result)

    result = morse_decode('....-/.----/----./....-/....-/.----/---../.----/....-/.----/-..../...--/....-/.----/----./..---/-..../..---/..---/...--/--.../....-')
    print(result)

test_encoder()
