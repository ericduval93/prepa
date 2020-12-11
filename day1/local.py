#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import os

def Local():
    # foo = 10
    Local2()
    print("Local() :: foo is : {}".format(foo))

def Local2():
    foo = 200
    print("Local2() :: foo is : {}".format(foo))

foo = 20
Local()
Local2()
print("Main() :: foo is : {}".format(foo))

exit(0)
