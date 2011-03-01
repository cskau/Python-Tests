#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

input_size = 2000000
table_height = 20

t_base = time.time()

table = [ [ 0 for y in range(table_height)] for x in range(input_size) ]

t_now = time.time()
print t_now-t_base

table = [ [ 0 for y in xrange(table_height)] for x in xrange(input_size) ]

t_now = time.time()
print t_now-t_base

for r in table:
  for c in r:
    if c == 0:
      1 + 1

t_now = time.time()
print t_now-t_base
