# Changelog

## Release v2.0.3
 * Privatizing internal function calls.  Checking for existence of Jar file before loading jar.
 * Testing for multi-dimensional list if pickled list is loaded with alwas_list=True
 * Updated requirements, README, and version information
 * Hiding private members from Sphinx.

# Release 2.0.2
 * Added ability to use Jar class with Python 'with' statements

# Release 2.0.1
 * Backend code improvements

# Release 2.0
 * Compatible with Python2.7 and 3.5
 * Renamed Jar.dump to Jar.load and Jar.collect to Jar.dump to keep with normal pickle operations

# Release 1.3
 * Added *collapse* kwarg to Jar.collect() method for writing a list as a single pickle
 * Added **always_list** kwarg to Jar.dump() method

# Release 1.2
 * Added more path verification to \_\_init__ method
 * Added kwarg **always_list** to set Jar.always_list property
 * Updated \_always_list_ property to non-private **always_list**

# Release 1.1
 * Added Jar.exists() method for testing whether a Jar exists
 * Added Jar.remove() method for removing a Jar file if it exists
 * Added \_always_list_ property to ensure that Jars containing a single item return as a list

# Release 1.0
 * Initial Version of PickleJar
