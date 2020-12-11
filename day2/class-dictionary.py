#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

class Dictionary():
    def __init__(self):
        self.mydict = {}

    def newentry(self, word, definition):
        self.mydict[word] = definition

    def look(self, key):
        if key in self.mydict:
            print("{}".format(self.mydict[key]))
        else:
            print("Can't find new entry for {}".format(key))

d = Dictionary()
d.newentry("Apple", "A fruit")
d.look( "Apple" )
d.newentry("Soccer", "A sport")
d.look( "Soccer" )
d.look( "Hi" )
d.look( "Ball" )
d.newentry("soccer", "a sport")
d.look( "soccer" )


exit(0)
