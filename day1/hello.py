#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import os

def Hello( ): # {
    print("Hello world !")
#}

def Input( foo ): # {
    print("What is your {}".format(foo), end='? ')
    return( input() )
#}

Hello()
name = Input( 'name' )
print("Your name is {}".format(name))

exit(0)
