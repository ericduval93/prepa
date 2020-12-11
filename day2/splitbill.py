#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

def split_the_bill(x):
    mykey = sorted(x, key=x.get)
    mymin = x[mykey[0]]
    mymid = x[mykey[1]]
    mymax = x[mykey[2]]

    return( {mykey[2]:mymax-mymid, mykey[1]: 0, mykey[0]: mymin-mymid} )

dict1 = {'A': 20, 'B': 15, 'C': 10}
dict2 = {'A': 40, 'B': 25, 'X': 10}

foo = split_the_bill( dict1 )
print("foo( dict1 ) : {}".format(foo))
bar = split_the_bill( dict2 )
print("bar( dict1 ) : {}".format(bar))

exit(0)
