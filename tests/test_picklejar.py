#!/usr/bin/env python2
# coding=utf-8
"""Unit Tests for picklejar Python Module"""
__author__ = 'Jesse Almanrode'

import os
import sys
import unittest

here = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(here)
sys.path.append(project)
import picklejar

tmploc = '/tmp/test.pjar'

pkldata = ['string', 1, {'dict': 'value'}]
pklappend = ['another', 'list']


class TestPickleJar(unittest.TestCase):

    def setUp(self):
        self.pkls = picklejar.Jar(tmploc)

    def test_000_exists(self):
        self.setUp()
        self.assertFalse(self.pkls.exists())

    def test_001_new(self):
        self.setUp()
        self.assertFalse(self.pkls.exists())
        self.pkls.collect(pkldata)

    def test_002_append(self):
        self.setUp()
        self.assertTrue(self.pkls.exists())
        self.pkls.collect(pkldata)

    def test_003_read(self):
        self.setUp()
        self.assertTrue(self.pkls.exists())
        self.assertIsInstance(self.pkls.dump(), list)

    def test_004_start(self):
        self.setUp()
        self.assertTrue(self.pkls.exists())
        self.pkls.collect('test', newjar=True)

    def test_005_single(self):
        self.setUp()
        self.assertFalse(self.pkls._always_list_)
        self.assertTrue(self.pkls.exists())
        self.pkls.dump()

    def test_006_single_list(self):
        self.setUp()
        self.pkls._always_list_ = True
        self.assertTrue(self.pkls.exists())
        self.assertIsInstance(self.pkls.dump(), list)

    def test_007_remove(self):
        self.setUp()
        self.assertTrue(self.pkls.exists())
        self.pkls.remove()
        self.assertFalse(self.pkls.exists())


if __name__ == '__main__':
    unittest.main(failfast=True)
