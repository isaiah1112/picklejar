# Changelog

## Release 3.1.0
 * Updated Makefile to use non-literal variables. [a49742c]
 * Updated Copyright [b040071]
 * Removed `requirements.txt` and `setup.py`, replaced with `pyproject.toml` [dea545f]
 * Updated pip install commands in Bitbuckets Pipelines [1bce391]
 * Removing Python3.7 from BitBucket Pipelines [e89711d]
 * Updated Bitbucket Pipelines to use Poetry [51dc57e]
 * Removed install, install-dev, and test-init Makefile targets. [0fdc325]
 * Updated bitbucket-pipelines to publish to PyPI instead of using build/twine [e526daa]
 * Updated order of pipeline execution in release/* branches. [40b1555]

## Release 3.0.1
 * Moved Build Documentation step to release branches [325ed38]
 * Updated Makefile to include `docker-test-[py37-py310]` targets [60ca475]
 * Adding Flake8 Linting to Makefile and Pipelines for release branches [e5d0dc1]
 * Adding Python3.11.0rc2 to testing [c3ec8c9]
 * Not running coverage command in automated tests [697f6a7]
 * Bumping to Python3.11 image [fa0fe42]

## Release 3.0.0
 * Adding Python3.10 to testing [a56ed8a]
 * Updated requirements [e89c737]
 * Reconfigured Bitbucket Pipelines to not use tox [ef55ad9]
 * Dropping Python2.7 in addition to Python3.6 [215c267]
 * Added `Makefile` for common actions [db7946c]
 * Updated `setup.py` file to pull in README, set python_requires, etc. [69d4e3c]
 * Removed localized imports of module for test_picklejar.py [56ca5ee]
 * Added typing hints to picklejar [fa088e4]
 * Removed `always_list` property in favor of kwarg when using load [8adeb5f]
 * Using new class definition style [cba6b22]
 * Updated unittests for picklejar [dffe71d]
 * Renamed `newjar` kwarg to `new_jar` [acad7e4]
 * Removing docs for `always_list` in Jar object. [fe69b96]


## Release 2.1.2
 * Added Python3.9 support [59bd072]
 * Added twine to pip deployment process [2031b72]

## Release 2.1.1
 * Added Python3.8 support [c489127]

## Release 2.1
 * Adding Python3.4 and Python3.5 to testing [98efc97]
 * Updated requirements [50203d3]

## Release 2.0.10
 * Fixing typo [abb6260]
 * Adding pypy to Bitbucket-pipelines.yml [fe61b23]
 * Fixing BitBucket Pipelines for PyPy tests [57a9f02]
 * Making sure the production pipeline is updated too! [0ebe8f1]
 * Testing build against Python 3.7 [062f14f]
 * Re-ordering tests [d1f84c1]
 * Updating requirements and bumping version [e1e2784]

## Release 2.0.9
 * Updated version and requirements [ded32d1]

## Release 2.0.8
 * Updated requirements [af55801]

## Release 2.0.7
 * Updated documentation URL [0a06c46]

## Release 2.0.6
 * Updating requirements (new version of dill is available) [1498c9c]

## Release 2.0.5
 * Updating unittests to start using mock module. [39a6593]
 * Setting up documentation tox environment [168a079]
 * Reconfiguring bitbucket pipelines for deployment on push of master branch. [f1995ff]
 * Trimming down requirements for tox. [fbf3521]
 * Fixing `deploy.bash` so it works to publish to PyPi [447eeba]

## Release 2.0.4
 * Using tox for automated testing.  Support for Python2.6 and Python3.5 verified. [d4427b8]
 * bitbucket-pipelines.yml created online with Bitbucket [9c3d0dd]
 * Updated version info, requirements, and compatibility matrixes! [37e06c4]
 * Updated some comments [458b2ca]

## Release 2.0.3
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
