#!/usr/bin/env python
# coding=utf-8
"""UnitTests for picklejar Python Module
"""

import os
import sys
import unittest
import picklejar

__author__ = 'Jesse Almanrode (jesse@almanrode.com)'

# Globals
testloc = '/tmp/pkljar-test.pkl'
test_data = ['string', 1, {'dict': 'value'}]
test_list = ['another', 'list']


class TestPickleJar(unittest.TestCase):

    def setUp(self):
        """ Init a new Jar object
        :return: Jar Object
        """
        self.pkls = picklejar.Jar(testloc)
        pass

    def test_000_exists(self):
        """ Test to ensure the test Jar doesn't already exist
        :return: Jar.exists is False
        """
        assert self.pkls.exists() is False
        pass

    def test_001_new(self):
        """ Add test_data to new pkle file
        :return: Jar.collect() is True
        """
        global test_data
        assert self.pkls.exists() is False
        assert self.pkls.collect(test_data) is True
        pass

    def test_002_append(self):
        """ Test whether we can append another set of data to the Jar
        :return: Jar.collect is True
        """
        global test_list
        assert self.pkls.exists() is True
        assert self.pkls.collect(test_list)
        pass

    def test_003_read(self):
        """ Test whether we can read data from the Jar
        :return: Jar.dump() is list
        """
        assert self.pkls.exists() is True
        assert type(self.pkls.dump()) is list
        pass

    def test_004_start(self):
        """ Overwrite an existing Jar file
        :return: Jar.collect(newjar=True) is True
        """
        assert self.pkls.exists() is True
        assert self.pkls.collect('test string', newjar=True) is True
        pass

    def test_005_single(self):
        """ Return a single item from a Jar (in the test case a string) as the original type (a string)
        :return: Jar.dump() is str
        """
        assert self.pkls.exists() is True
        assert self.pkls._always_list_ is False
        assert type(self.pkls.dump()) in (str, basestring)
        pass

    def test_006_single_list(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        :return: Jar.dump() is list
        """
        assert self.pkls.exists() is True
        self.pkls._always_list_ = True
        assert self.pkls._always_list_ is True
        assert type(self.pkls.dump()) is list
        pass

    def test_007_remove(self):
        """ Remove an existing Jar file
        :return: Jar.remove is True
        """
        assert self.pkls.exists() is True
        assert self.pkls.remove() is True
        assert self.pkls.exists() is False
        pass


if __name__ == '__main__':
    unittest.main()
