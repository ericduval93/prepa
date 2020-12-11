#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import os

def DivideBy(foo):
    try:
        return( 100 / foo )
    except ZeroDivisionError as e:
        print( e )
    except ValueError as e:
        print( e )
    except TypeError as e:
        print( e )

print("10 :: {}".format(DivideBy( 10 )))
print("0 :: {}".format(DivideBy( 0 )))
print("100 :: {}".format(DivideBy( 100 )))
print("toto :: {}".format(DivideBy( 'toto' )))
print("1 :: {}".format(DivideBy( 1 )))


exit(0)
