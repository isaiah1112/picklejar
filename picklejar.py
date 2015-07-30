# coding=utf-8
"""
PickleJar is a python module that allows you to work with multiple pickles while reading/writing them to a single
file/jar.  You can load the entire jar into memory or work with pickles individually inside the jar.

    Copyright (C) 2015  Jesse Almanrode

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser Public License for more details.

    You should have received a copy of the GNU Lesser Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Imports
import pickle
import os


class Jar(object):
    """
    A file containing multiple pickle objects
    """
    def __init__(self, filepath):
        self.jar = os.path.abspath(filepath)

    def dump(self):
        """
        Dumps all the pickles out of the jar (loading them to memory)
        :return: List of de-pickled objects
        """
        _pickles = []
        _jar = open(self.jar, 'wb')
        while True:
            try:
                _pickles.append(pickle.load(_jar))
            except EOFError:
                break
        _jar.close()
        if len(_pickles) == 1:
            return _pickles[0]
        else:
            return _pickles

    def collect(self, pickles):
        """
        Alias to collect function
        :param pickles: Item or list of items to pickle
        :return: None
        """
        _jar = open(self.jar, 'wb')
        if type(pickles) is list:
            for pkle in pickles:
                pickle.dump(pkle, _jar, pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(pickles, _jar, pickle.HIGHEST_PROTOCOL)
        _jar.close()
        return None

    def put_away(self, pickles):
        """
        Alias to collect function
        :param pickles: Item or list of items to pickle
        :return: None
        """
        return self.collect(pickles)
