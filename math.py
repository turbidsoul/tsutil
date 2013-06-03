# -*- coding: utf8 -*-


def cal_pi(n=999999):
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


print(cal_pi())
