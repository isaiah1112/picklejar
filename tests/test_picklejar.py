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
test_data = ['string', 1, {'key': 'value'}]
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
        self.assertFalse(self.pkls.exists())
        pass

    def test_001_new(self):
        """ Add test_data to new pkle file
        :return: Jar.dump() is True
        """
        global test_data
        self.assertFalse(self.pkls.exists())
        self.assertTrue(self.pkls.dump(test_data))
        pass

    def test_002_append(self):
        """ Test whether we can append another set of data to the Jar
        :return: Jar.dump() is True
        """
        global test_list
        self.assertTrue(self.pkls.exists())
        self.assertTrue(self.pkls.dump(test_list))
        pass

    def test_003_read(self):
        """ Test whether we can read data from the Jar
        :return: Jar.load() is list
        """
        self.assertTrue(self.pkls.exists())
        self.assertIsInstance(self.pkls.load(), list)
        pass

    def test_004_start(self):
        """ Overwrite an existing Jar file
        :return: Jar.dump(newjar=True) is True
        """
        self.assertTrue(self.pkls.exists())
        self.assertTrue(self.pkls.dump('test string', newjar=True))
        pass

    def test_005_single(self):
        """ Return a single item from a Jar (in the test case a string) as the original type (a string)
        :return: Jar.load() is str
        """
        self.assertTrue(self.pkls.exists())
        self.assertFalse(self.pkls.always_list)
        self.assertIsInstance(self.pkls.load(), str)
        pass

    def test_006_single_list_property(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        :return: Jar.load() is list
        """
        self.assertTrue(self.pkls.exists())
        self.pkls.always_list = True
        self.assertTrue(self.pkls.always_list)
        self.assertIsInstance(self.pkls.load(), list)
        pass

    def test_007_single_list(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        :return: Jar.load(always_list=True) is list
        """
        self.assertTrue(self.pkls.exists())
        self.pkls.always_list = False
        self.assertFalse(self.pkls.always_list)
        self.assertIsInstance(self.pkls.load(always_list=True), list)
        pass

    def test_008_collapse(self):
        """ Ensure a list of objects is written as a single pickle object
        :return: len(self.pkls.load()) == 2
        """
        self.assertTrue(self.pkls.exists())
        self.assertTrue(self.pkls.dump(test_list, newjar=True, collapse=True))
        self.assertIsInstance(self.pkls.load(), list)
        self.assertEqual(len(self.pkls.load()), 2)
        pass

    def test_009_remove(self):
        """ Clean up after all tests complete
        :return: Jar.remove is True
        """
        self.assertTrue(self.pkls.exists())
        self.assertTrue(self.pkls.remove())
        self.assertFalse(self.pkls.exists())
        pass

if __name__ == '__main__':
    unittest.main()
