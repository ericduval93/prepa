#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money ):
        if self.balance < money:
            print("{} has no enought money!".format(self.name))
            return
        self.balance -= money
        print( "{} has {}.".format(self.name,self.balance) )

    def check(self, name, money):
        if not isinstance(name, User):
            print("{} doesn't exist!".format(name.name))
            return

        if not name.checking_account:
            print("{} has check account at False!".format(name.name))
            return

        if name.balance < money:
            print("{} has no enought money! balance={} / money={}".format(name.name,name.balance, money))
            return

        self.balance += money
        name.balance -= money

        print( "{} has {} and {} has {}.".format(self.name,self.balance,name.name,name.balance) )

    def add_cash(self, money):
        self.balance += int(money)
        print( "{} has {}.".format(self.name,self.balance) )


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

Jeff.withdraw(2)
Joe.check(Jeff, 50)
Jeff.check(Joe, 80)
Joe.check(Jeff, 100)
Jeff.add_cash(20.00)

exit(0)
