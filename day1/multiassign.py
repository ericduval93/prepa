#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

foo = [1,2,3,4,5]
v1, v2, v3 = foo[:3]
print("v1={} / v2={} / v3={}".format(v1,v2,v3))

v1, v2, v3 = 'valV1','valV2','valV3'
print("v1={} / v2={} / v3={}".format(v1,v2,v3))

a = 'AAA'
b = 'BBB'
print("Before permutation: a = {} / b = {}".format(a,b))
a,b = b,a
print("After permutation: a = {} / b = {}".format(a,b))

exit( 0 )
