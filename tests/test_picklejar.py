#!/usr/bin/env python
# coding=utf-8
"""UnitTests for picklejar Python Module
"""

import os
import sys
import unittest
try:
    import picklejar
except ImportError:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)
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
        assert isinstance(self.pkls.dump(), list)
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
        assert self.pkls.always_list is False
        assert isinstance(self.pkls.dump(), (str, basestring))
        pass

    def test_006_single_list_property(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        :return: Jar.dump() is list
        """
        assert self.pkls.exists() is True
        self.pkls.always_list = True
        assert self.pkls.always_list is True
        assert isinstance(self.pkls.dump(), list)
        pass

    def test_007_single_list(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        :return: Jar.dump(always_list=True) is list
        """
        assert self.pkls.exists() is True
        self.pkls.always_list = False
        assert self.pkls.always_list is False
        assert isinstance(self.pkls.dump(always_list=True), list)
        pass

    def test_008_collapse(self):
        """ Ensure a list of objects is written as a single pickle object
        :return: len(self.pkls.dump()) == 2
        """
        assert self.pkls.exists() is True
        assert self.pkls.collect(test_list, newjar=True, collapse=True) is True
        assert isinstance(self.pkls.dump(), list)
        assert len(self.pkls.dump()) == 2
        pass

    def test_009_remove(self):
        """ Clean up after all tests complete
        :return: Jar.remove is True
        """
        assert self.pkls.exists() is True
        assert self.pkls.remove() is True
        assert self.pkls.exists() is False
        pass

if __name__ == '__main__':
    unittest.main()
