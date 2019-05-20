# TNP - That New Program
> Interactive program of generating conjectures about simple graphs.

## Installation

To install dependencies, run:

```sh
$ make install
```

For development specific dependencies, install by running:

```sh
$ make install-dev
```

To install all dependencies at once, run:

```sh
$ make install-all
```

### Running the program

To run the program:

```sh
$ python TNP.py
```

## Code Quality

This project uses `flake8` and `black` to check code quality and code formatting.

To run `flake8`:

```sh
$ make lint
```

The check the formatting, run:

```sh
$ make check-formatting
```

To run `black` on the source code:

```sh
$ make format
```

## Running Tests

To run the tests, you must first install the `tnp` module locally:

```sh
$ pip install -e .
```

This installs the module locally in editable mode, so that ay local changes to the source are automatically reflected in the local installation.

> **IMPORTANT**: Notice the `.` at the end of the above command. Don't leave this out!

Once installed, you can run the test suite:

```sh
$ make test
```
