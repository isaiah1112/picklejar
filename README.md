![logo](./logo.png "PickleJar")

A python module that allows you to work with multiple pickles while reading/writing them to a single 
file/jar.

## License
[picklejar] is released under the [GNU Lesser General Public License v3.0], see the file LICENSE and LICENSE.lesser 
for the license text.

## Compatibility
I attempt to maintain support for all [Supported versions of Python](https://devguide.python.org/versions/).

# Installation/Getting Started
The most straightforward way to get the picklejar module working for you is:
```commandline
pip install picklejar
```
or, for a local installation (after cloning the repo):
```commandline
make install
```

# Documentation
All documentation for using picklejar can be found at [ReadTheDocs](http://picklejar.readthedocs.io/)

# Contributing
Code contributions are encouraged: please feel free to [fork the
project](https://github.com/isaiah1112/picklejar) and submit pull requests to the **develop** branch.

Report any issues or feature requests on the [BitBucket bug
tracker](https://github.com/isaiah1112/picklejar/issues). Please include a minimal (not-) 
working example which reproduces the bug and, if appropriate, the traceback information.  Please do not request features 
already being worked towards.

## Testing
To run the tests for [picklejar] locally with your installed version of python, simply run:
```commandline
make test
```

To run tests across different versions of Python via [Docker](https://www.docker.com), install and start Docker, 
then run:
```commandline
make docker-test-all
```

[GNU Lesser General Public License v3.0]: http://choosealicense.com/licenses/lgpl-3.0/ "LGPL v3"

[picklejar]: https://github.com/isaiah1112/picklejar "picklejar Module"
