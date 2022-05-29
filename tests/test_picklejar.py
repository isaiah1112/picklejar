#!/usr/bin/env python
# coding=utf-8
"""UnitTests for picklejar Python Module
"""

import mock
import picklejar
import unittest
import warnings

__author__ = 'Jesse Almanrode (jesse@almanrode.com)'


class TestPickleJar(unittest.TestCase):

    def setUp(self):
        """ Init a new picklejar.Jar object
        """
        self.pkls = picklejar.Jar('/tmp/pkljar-test.pkl')
        pass

    @mock.patch('picklejar.os.path')
    def test_exists(self, mock_path):
        """ Test exists method of picklejar
        """
        mock_path.exists.return_value = False
        self.assertFalse(self.pkls.exists())
        mock_path.exists.return_value = True
        self.assertTrue(self.pkls.exists())
        pass

    def test_new(self):
        """ Add test_data to new pkle file
        """
        with mock.patch('picklejar.open', mock.mock_open(), create=True):
            self.assertTrue(self.pkls.dump(['string', 1, {'key': 'value'}]))
        pass

    @mock.patch('picklejar.os.path')
    def test_read(self, mock_path):
        """ Test whether we can read data from the Jar
        """
        mock_path.exists.return_value = True
        with mock.patch('picklejar.open', mock.mock_open(read_data=None), create=True):
            with mock.patch('picklejar.dill.load', mock.Mock(side_effect=['test', 'data', EOFError()])):
                self.assertTrue(isinstance(self.pkls.load(), list))
        pass

    def test_startfresh(self):
        """ Overwrite an existing Jar file
        """
        with mock.patch('picklejar.open', mock.mock_open(), create=True):
            self.assertTrue(self.pkls.dump('test string', new_jar=True))
        pass

    @mock.patch('picklejar.os.path')
    def test_single(self, mock_path):
        """ Return a single item from a Jar (in the test case a string) as the original type (a string)
        """
        mock_path.exists.return_value = True
        with mock.patch('picklejar.open', mock.mock_open(read_data=None), create=True):
            with mock.patch('picklejar.dill.load', mock.Mock(side_effect=['foo', EOFError()])):
                self.assertTrue(isinstance(self.pkls.load(always_list=False), str))
        pass

    @mock.patch('picklejar.os.path')
    def test_single_list(self, mock_path):
        """ Return a single item from a Jar (in the test case a string) as a list with a single item (the string)
        """
        mock_path.exists.return_value = True
        with mock.patch('picklejar.open', mock.mock_open(read_data=None), create=True):
            with mock.patch('picklejar.dill.load', mock.Mock(side_effect=['foo', EOFError()])):
                self.assertTrue(isinstance(self.pkls.load(always_list=True), list))
        pass

    def test_collapse(self):
        """ Ensure a list of objects is written as a single pickle object
        """
        with mock.patch('picklejar.open', mock.mock_open(), create=True):
            self.assertTrue(self.pkls.dump([1, 2, 3], new_jar=True, collapse=True))
        pass

    @mock.patch('picklejar.os.path')
    def test_multi_dimensional_list(self, mock_path):
        """ Test whether a pickled list is returned as a two-dimensional list if always_list == True
        """
        mock_path.exists.return_value = True
        with mock.patch('picklejar.open', mock.mock_open(), create=True):
            with mock.patch('picklejar.dill.load', mock.Mock(side_effect=[[1, 2], EOFError()])):
                r = self.pkls.load(always_list=True)
                self.assertEqual(len(r), 1)
                self.assertEqual(len(r[0]), 2)
        pass

    @mock.patch('picklejar.os.path')
    @mock.patch('picklejar.os')
    def test_remove_jar(self, mock_path, mock_os):
        """ Clean up after all tests complete
        """
        mock_path.exists.return_value = True
        self.assertTrue(self.pkls.exists())
        mock_os.remove.return_value = True
        self.assertTrue(self.pkls.remove())
        pass


if __name__ == '__main__':
    with warnings.catch_warnings(record=True):
        unittest.main()
