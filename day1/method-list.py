#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

foo = ['foo1', 'foo2', 'foo3', 'foo4', 'foo5', 'foo6']
bar = ['bar1', 'bar2', 'bar3', 'bar4', 'bar5', 'bar6']

print( "foo = {}".format(foo) )
print( "bar = {}".format(bar) )

print( "Index method  = {}".format(bar.index('bar3')) )

bar.append('bar7')
print( "Append method  = {}".format(bar))

bar.insert(2,'bar2.2')
print( "Insert method  = {}".format(bar))

bar.remove('bar2.2')
print( "Remove method  = {}".format(bar))

foo2 = [7,3,8,9,-1,-7,23]
foo2.sort()
print( "Sort method  = {}".format(foo2))

foo2.sort(reverse=True)
print( "reverse Sort method  = {}".format(foo2))

foo3 = ['a', 'z', 'A', 'Z' ]
foo3.sort()
print( "Sort method  = {}".format(foo3))

foo3.sort(key=str.lower)
print( "Sort lower method  = {}".format(foo3))

foo3.sort(key=str.lower,reverse=True)
print( "reverse Sort lower method  = {}".format(foo3))

exit(0)
