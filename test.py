# -*- coding: utf8 -*-
from math2 import Pi
from encoder import morse_encode, morse_decode


def test_math2():
    pi = Pi()
    print(pi.leibniz_pi(999999))
    print(pi.wallis_pi(999999))


def test_encoder():

    result = morse_encode('4194418141634192622374')
    print(result)

    result = morse_decode(result)
    print(result)

    result = morse_decode('....-/.----/----./....-/....-/.----/---../.----/....-/.----/-..../...--/....-/.----/----./..---/-..../..---/..---/...--/--.../....-')
    print(result)

test_math2()
