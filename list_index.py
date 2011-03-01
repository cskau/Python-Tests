#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time, timeit

states = [1,2,3,45,6,7,99,0]
states_index = states.index
states_index_dict = {1:0,2:1,3:2,45:3,6:4,7:5,99:6,0:7}

def test1():
  states.index(99)

def test2():
  states_index(99)

def test3():
  states_index_dict[99]

if __name__=='__main__':
    from timeit import Timer
    t1 = Timer("test1()", "from __main__ import test1")
    print "%.2f usec/pass" % (1000000 * t1.timeit(number=100000)/100000)
    t2 = Timer("test2()", "from __main__ import test2")
    print "%.2f usec/pass" % (1000000 * t2.timeit(number=100000)/100000)
    t3 = Timer("test3()", "from __main__ import test3")
    print "%.2f usec/pass" % (1000000 * t3.timeit(number=100000)/100000)
