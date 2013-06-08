# -*- coding: utf8 -*-

# -*- coding: utf8 -*-

class Pi(object):
    """
    计算pi
    """

    def leibniz_pi(self, n=100):
        """
        `1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4` = `pi/4 = sum_{n=0}^{oo} (-1)^n/(2n+1)`
        """
        m_pi = 0
        for x in range(0, n + 1):
            m_pi += (-1.0) ** x / (2.0 * x + 1.0)
        return m_pi * 4


    def wallis_pi(self, n=100):
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

    def spigot_pi(self, n=1):
        p = 0.0
        for k in range(0, n + 1):
            t1 = (4.0 / (8.0 * k + 1) - 2.0 / (8.0 * k +3) - 1.0 / (8.0 * k + 5) - 1.0 / (8.0 * k + 6))
            print(16.0 ** k)
            t2 = 1.0 / (16.0**k)
            p += t2 * t1
        return p
