#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

foo = [1,2,3,4,5]
bar = [foo, [6,7,8,9]]

print( "foo = {}".format(foo) )
print( "bar = {}".format(bar) )
print("foo[0] = {}".format(foo[0]))
print("bar[0] = {}".format(bar[0]))
print("bar[1][0] = {}".format(bar[1][0]))
print("last elem de foo[-1] = {}".format(foo[-1]))
print("last elem de bar[-1] = {}".format(bar[-1]))
print("One elem de foo[-3] = {}".format(foo[-3]))
print("One elem de bar[-1][-2] = {}".format(bar[-1][-2]))

foo[2] =  'New value'
print( "foo = {}".format(foo) )

foo[1:2] = ['R1','R2' ]
print( "foo = {}".format(foo) )

print( "foo[:2] = {}".format(foo[:2]) )
print( "foo[3:] = {}".format(foo[3:]) )

print( "Before del foo[2] = {}".format(foo) )
del foo[2]
print( "After del foo[2] = {}".format(foo) )

print( "len de foo = {}".format(len(foo)) )
print( "len de bar = {}".format(len(bar)) )

print( "foo + bar = {}".format(foo + bar) )
print( "(foo + bar)*2 = {}".format((foo + bar)*2) )

print( "list('Hello') = {}".format(list('Hello')) )

if "R1" in foo:
    print( "R1 is in foo : {}".format(foo) )
else:
    print( "R1 is NOT in foo : {}".format(foo) )

for i in foo:
    print("for foo: {}".format(i))

print("range foo: {}".format(list(range(4))))

print( "foo = {}".format(foo) )
for i in range(len(foo)):
    print("for range len foo: index={} / value={}".format(i,foo[i]))


exit(0)
