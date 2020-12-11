#!/usr/bin/python3

# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

class Router(object):
    pass
class bind():
    pass
class runRequest():
    pass

router = Router()
router.bind('/hello', 'GET', lambda: 'hello world')
router.bind('/login', 'GET', lambda: 'Please log-in.')
router.runRequest('/hello', 'GET') # 'hello world'
router.runRequest('/login', 'GET') # 'Please log-in.'

router = Router()
router.bind('/vote', 'POST', lambda: 'Voted.')
router.bind('/comment', 'POST', lambda:  'Comment sent.')
router.runRequest('/vote', 'POST') # 'Voted.'
router.runRequest('/comment', 'POST') # 'Comment sent.'

router = Router()
router.bind('/login', 'GET', lambda: 'Please log-in.')
router.bind('/login', 'POST', lambda: 'Logging-in.')
router.runRequest('/login', 'GET') # 'Please log-in.'
router.runRequest('/login', 'POST') # 'Logging-in.'


router = Router()
router.bind('/page', 'GET', lambda: 'First binding.')
router.bind('/page', 'GET', lambda: 'Modified binding.')
router.runRequest('/page', 'GET') # 'Modified binding.'

exit(0)

# ------------------------------------------------------
# Test.describe('Should handle GET routes')
# router = Router()
# router.bind('/hello', 'GET', lambda: 'hello world')
# router.bind('/login', 'GET', lambda: 'Please log-in.')
#
# Test.assert_equals(router.runRequest('/hello', 'GET'), 'hello world')
# Test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.')
#
# Test.describe('Should handle POST routes')
#
# router = Router()
# router.bind('/vote', 'POST', lambda: 'Voted.')
# router.bind('/comment', 'POST', lambda:  'Comment sent.')
#
# Test.assert_equals(router.runRequest('/vote', 'POST'), 'Voted.')
# Test.assert_equals(router.runRequest('/comment', 'POST'), 'Comment sent.')
#
# Test.describe('Should handle mixed routes.')
#
# router = Router()
# router.bind('/login', 'GET', lambda: 'Please log-in.')
# router.bind('/login', 'POST', lambda: 'Logging-in.')
#
# Test.assert_equals(router.runRequest('/login', 'GET'), 'Please log-in.');
# Test.assert_equals(router.runRequest('/login', 'POST'), 'Logging-in.');
#
#
# Test.describe('Should return 404 for non-existing routes.')
#
# router = Router()
# Test.assert_equals(router.runRequest('/this-url-does-not-exist', 'GET'), 'Error 404: Not Found');
#
#
# Test.describe('Should modify existing routes')
#
# router = Router()
# router.bind('/page', 'GET', lambda: 'First binding.')
# router.bind('/page', 'GET', lambda: 'Modified binding.')
#
# Test.assert_equals(router.runRequest('/page', 'GET'), 'Modified binding.');
#
