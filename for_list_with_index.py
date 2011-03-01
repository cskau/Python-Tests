#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import timeit

MAGIC_NUMBER1,MAGIC_NUMBER2 = 10000000,1000000

test_data = ['a','c','b','f','g','mrh','','g']

def test1():
  for i in range(len(test_data)):
    test_data[i]

def test2():
  for i in xrange(len(test_data)):
    test_data[i]

def test3():
  for i,td in [ (i,test_data[i]) for i in xrange(len(test_data)) ]:
    td

def test4():
  for i,td in enumerate(test_data):
    td


if __name__=='__main__':
  from timeit import Timer
  t1 = Timer("test1()", "from __main__ import test1")
  print "%.2f usec/pass" % (MAGIC_NUMBER1 * t1.timeit(number=MAGIC_NUMBER2)/MAGIC_NUMBER2)
  t2 = Timer("test2()", "from __main__ import test2")
  print "%.2f usec/pass" % (MAGIC_NUMBER1 * t2.timeit(number=MAGIC_NUMBER2)/MAGIC_NUMBER2)
  t3 = Timer("test3()", "from __main__ import test3")
  print "%.2f usec/pass" % (MAGIC_NUMBER1 * t3.timeit(number=MAGIC_NUMBER2)/MAGIC_NUMBER2)
  t4 = Timer("test4()", "from __main__ import test4")
  print "%.2f usec/pass" % (MAGIC_NUMBER1 * t4.timeit(number=MAGIC_NUMBER2)/MAGIC_NUMBER2)
