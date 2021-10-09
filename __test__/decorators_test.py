# -*- coding: utf-8 -*-
from tsutil.decorators import singleton, singleton_fun
from unittest import TestCase, main

@singleton
class SingleSample(object):
  pass

@singleton_fun
def single_sample(a, b):
  return a + b

class SingleTest(TestCase):
  
  def test_singleclass(self):
    s1 = SingleSample()
    s2 = SingleSample()
    self.assertEqual(s1, s2)

  def test_singlefunc(self):
    s1 = single_sample(1, 2)
    s2 = single_sample(1, 2)
    self.assertEqual(s1, s2)
  
  def test_singlefunc2(self):
    s1 = single_sample(1, 2)
    s2 = single_sample(1, 2)
    
    self.assertIs(s1, s2)
  
  def test_singlefunc3(self):
    s1 = single_sample(2, 2)
    s2 = single_sample(2, 3)
    
    self.assertIsNot(s1, s2)

  def test_singlefunc4(self):
    s1 = single_sample(2, 2)
    s2 = single_sample(2, 3)
    
    self.assertIsNot(hash(s1), hash(s2))

if __name__ == "__main__":
  main()
