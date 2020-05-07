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

### Running the program

To run the program:

```sh
$ python write_on_the_wall.py
```
