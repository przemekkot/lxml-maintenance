import unittest
from lxml.tests.common_imports import doctest
from lxml.etree import LIBXML_VERSION

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([doctest.DocFileSuite('test_clean.txt')])
    if LIBXML_VERSION <= (2,6,28):
        suite.addTests([doctest.DocFileSuite('test_clean_embed.txt')])
    return suite