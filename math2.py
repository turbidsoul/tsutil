# -*- coding: utf8 -*-


def leibniz_pi(n=100):
    """
    `1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4`
    """
    m_pi = 0
    op = "add"
    for x in range(0, n):
        if op == "add":
            m_pi += 1.0 / (1.0 + x * 2.0)
            op = "sub"
        elif op == "sub":
            m_pi -= 1.0 / (1.0 + x * 2.0)
            op = "add"
    return m_pi * 4


def wallis_pi(n=100):
    """
    `2 2/3 4/3 4/5 6/5 6/7 8/7 8/9 ... = pi/2`
    """
    p = 1.0
    a = 2.0
    b = 1.0
    for x in xrange(1, n):
        p *= a / b
        a, b = b + 1, a + 1

    return p * 2.0
