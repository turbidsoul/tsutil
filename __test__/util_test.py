# -*- coding: utf-8 -*-
from tsutil.util import singleton
from unittest import TestCase, main

@singleton
class SingleSample(object):
  pass

class SingleTest(TestCase):
  
  def test_single(self):
    s1 = SingleSample()
    s2 = SingleSample()
    
    self.assertEqual(s1, s2)

if __name__ == "__main__":
  main()
