# Changelog

## Release v2.0.7
 * Updated documentation URL [0a06c46]

## Release v2.0.6
 * Updating requirements (new version of dill is available) [1498c9c]

## Release v2.0.5
 * Updating unittests to start using mock module. [39a6593]
 * Setting up documentation tox environment [168a079]
 * Reconfiguring bitbucket pipelines for deployment on push of master branch. [f1995ff]
 * Trimming down requirements for tox. [fbf3521]
 * Fixing deploy.bash so it works to publish to PyPi [447eeba]

## Release v2.0.4
 * Using tox for automated testing.  Support for Python2.6 and Python3.5 verified. [d4427b8]
 * bitbucket-pipelines.yml created online with Bitbucket [9c3d0dd]
 * Updated version info, requirements, and compatibility matrixes! [37e06c4]
 * Updated some comments [458b2ca]

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
