#!/usr/bin/env python
"""UnitTests for picklejar Python Module
"""

import os
import tempfile
import unittest
import warnings
from unittest import mock

import picklejar

__author__ = 'Jesse Almanrode (jesse@almanrode.com)'


class TestPickleJar(unittest.TestCase):

    def setUp(self):
        """ Init a new picklejar.Jar object
        """
        # Use a temporary file for testing instead of /tmp
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, 'pkljar-test.pkl')
        self.pkls = picklejar.Jar(self.temp_file)

    def tearDown(self):
        """ Clean up temporary files
        """
        self.temp_dir.cleanup()

    def test_exists(self):
        """ Test exists method of picklejar
        """
        self.assertFalse(self.pkls.exists())
        with self.assertRaises(OSError):
            self.pkls.load()
        # Create the file
        self.pkls.dump('test data', new_jar=True)
        self.assertTrue(self.pkls.exists())

    def test_new(self):
        """ Add test_data to new pkle file
        """
        self.assertTrue(self.pkls.dump(['string', 1, {'key': 'value'}], new_jar=True))
        self.assertTrue(self.pkls.exists())

    def test_read(self):
        """ Test whether we can read data from the Jar
        """
        # Write some test data first
        self.pkls.dump(['test', 'data'], new_jar=True)
        # Now read it back
        result = self.pkls.load()
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, ['test', 'data'])

    def test_startfresh(self):
        """ Overwrite an existing Jar file
        """
        # Create initial file
        self.pkls.dump('initial data', new_jar=True)
        # Overwrite with new_jar=True
        self.assertTrue(self.pkls.dump('test string', new_jar=True))
        result = self.pkls.load()
        self.assertEqual(result, 'test string')

    def test_single(self):
        """ Return a single item from a Jar (in the test case a string) as the original type (a string)
        """
        self.pkls.dump('foo', new_jar=True)
        result = self.pkls.load(always_list=False)
        self.assertTrue(isinstance(result, str))
        self.assertEqual(result, 'foo')

    def test_single_list(self):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        """
        self.pkls.dump('foo', new_jar=True)
        result = self.pkls.load(always_list=True)
        self.assertTrue(isinstance(result, list))
        self.assertEqual(result, ['foo'])

    def test_collapse(self):
        """ Ensure a list of objects is written as a single pickle object
        """
        self.assertTrue(self.pkls.dump([1, 2, 3], new_jar=True, collapse=True))
        result = self.pkls.load()
        # With collapse=True, the list should be pickled as a single object
        self.assertEqual(result, [1, 2, 3])

    def test_multi_dimensional_list(self):
        """ Test whether a pickled list is returned as a two-dimensional list if always_list == True
        """
        # Write a list as a single pickle
        self.pkls.dump([1, 2], new_jar=True, collapse=True)
        r = self.pkls.load(always_list=True)
        self.assertEqual(len(r), 1)
        self.assertEqual(len(r[0]), 2)

    def test_remove_jar(self):
        """ Test removing a jar file
        """
        # Create a jar file first
        self.pkls.dump('test', new_jar=True)
        self.assertTrue(self.pkls.exists())
        # Remove it
        self.assertTrue(self.pkls.remove())
        self.assertFalse(self.pkls.exists())


if __name__ == '__main__':
    with warnings.catch_warnings(record=True):
        unittest.main()
