# -*- coding: utf-8 -*-
from unittest import TestCase, main
from tsutil.sequence import sequence


class TestSequence(TestCase):
  
  def test_seq(self):
    seq = sequence(1, 1)
    self.assertIsNotNone(seq)
    id1 = next(seq)
    id2 = next(seq)
    self.assertIsNotNone(id1)
    self.assertIsNotNone(id2)
    self.assertNotEqual(id1, id2)
  
  def test_seq2(self):
    seq1 = sequence(1, 1)
    seq2 = sequence(1, 1)
    id1, id2 = next(seq1), next(seq2)
    self.assertIsNotNone(id1)
    self.assertIsNotNone(id2)
    self.assertEqual(id1, id2)
 
  def test_seq3(self):
    seq1 = sequence(1, 1)
    seq2 = sequence(2, 1)
    id1, id2 = next(seq1), next(seq2)
    self.assertIsNotNone(id1)
    self.assertIsNotNone(id2)
    self.assertNotEqual(id1, id2)
  
  def test_seq4(self):
    seq1 = sequence(1, 1)
    seq2 = sequence(1, 2)
    id1, id2 = next(seq1), next(seq2)
    self.assertIsNotNone(id1)
    self.assertIsNotNone(id2)
    self.assertNotEqual(id1, id2)
    
  def test_seq5(self):
    seq1 = sequence(1, 1)
    seq2 = sequence(2, 2)
    id1, id2 = next(seq1), next(seq2)
    self.assertIsNotNone(id1)
    self.assertIsNotNone(id2)
    self.assertNotEqual(id1, id2)

if __name__ == "__main__":
  main()
